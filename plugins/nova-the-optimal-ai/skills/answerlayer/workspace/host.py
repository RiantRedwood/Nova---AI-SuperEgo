#!/usr/bin/env python3
"""Private loopback native-artifact display. No durable record store."""
from pathlib import Path
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from http.cookies import SimpleCookie
import argparse, json, secrets, sys, tempfile, subprocess, urllib.request, webbrowser, threading
import hashlib,os,stat
ROOT=Path(__file__).absolute().parent
def guard(path):
    path=Path(path).absolute()
    for node in [path,*path.parents]:
        value=node.lstat()
        if stat.S_ISLNK(value.st_mode) or getattr(value,'st_file_attributes',0)&1024:raise ValueError('Linked runtime refused: '+str(node))
    return path
guard(ROOT)
sys.path.insert(0,str(guard(ROOT.parent/'scripts')))
from io_contract import strict,dumps,LedgerError
from ledgerlib import validate
from launch_runtime import launch,RUNTIME_NONCE
identity=hashlib.sha256()
for current,dirs,names in os.walk(ROOT.parent,followlinks=False):
    dirs[:]=sorted(d for d in dirs if d!='__pycache__')
    for d in dirs:guard(Path(current)/d)
    for name in sorted(names):
        if name.endswith('.pyc'):continue
        path=guard(Path(current)/name)
        if not path.is_file():raise ValueError('Nonregular runtime file')
        identity.update(path.relative_to(ROOT.parent).as_posix().encode());identity.update(path.read_bytes())
RUNTIME_SHA=identity.hexdigest()
CONFIG=json.loads((ROOT/'desk.json').read_text(encoding='utf-8'))
TOKEN=secrets.token_urlsafe(32)
def validate_record(record):
    try:return validate(strict(record) if isinstance(record,str) else record)
    except (ValueError,UnicodeError,RecursionError) as error:return [str(error)]
class Handler(BaseHTTPRequestHandler):
    def log_message(self,*args): pass
    def reply(self,status,value,json_value=True):
        raw=json.dumps(value,ensure_ascii=False).encode() if json_value else value
        self.send_response(status); self.send_header('Content-Type','application/json; charset=utf-8' if json_value else 'text/html; charset=utf-8'); self.send_header('Cache-Control','no-store');
        if getattr(self,'issue_session',False):self.send_header('Set-Cookie',f'{self.cookie_name()}={TOKEN}; HttpOnly; SameSite=Strict; Path=/')
        self.send_header('X-Content-Type-Options','nosniff'); self.send_header('Referrer-Policy','no-referrer'); self.send_header('Content-Security-Policy',"default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; connect-src 'self'; img-src 'self' data:; frame-ancestors 'none'; base-uri 'none'; form-action 'none'"); self.end_headers(); self.wfile.write(raw)
    def static_asset(self, relative, mime):
        raw=guard(ROOT/relative).read_bytes()
        self.send_response(200)
        self.send_header('Content-Type',mime)
        self.send_header('Content-Length',str(len(raw)))
        self.send_header('Cache-Control','no-store')
        self.send_header('X-Content-Type-Options','nosniff')
        self.send_header('Referrer-Policy','no-referrer')
        self.end_headers()
        self.wfile.write(raw)
    def cookie_name(self):
        return 'desk_'+hashlib.sha256((CONFIG['id']+'|'+str(ROOT)).encode('utf-8')).hexdigest()[:16]+'_'+str(self.server.server_port)
    def authorized(self):
        origin=f'http://127.0.0.1:{self.server.server_port}'
        cookie=SimpleCookie();cookie.load(self.headers.get('Cookie',''));credential=cookie.get(self.cookie_name());valid=self.headers.get('X-Desk-Token')==TOKEN or (credential is not None and credential.value==TOKEN)
        return self.headers.get('Host')==origin.removeprefix('http://') and self.headers.get('Origin',origin)==origin and valid
    def do_GET(self):
        if self.headers.get('Host')!=f'127.0.0.1:{self.server.server_port}': return self.reply(403,{'error':'Unexpected host'})
        if self.path=='/api/health': return self.reply(200,{'product':CONFIG['id'],'version':CONFIG['version'],'workspace':str(ROOT),'mode':'native-file preparation; no persistent record store','runtime_sha256':RUNTIME_SHA,'instance':RUNTIME_NONCE})
        if self.path=='/': return self.reply(200,(ROOT/'index.html').read_bytes(),False)
        if self.path=='/refinement.css': return self.static_asset('refinement.css','text/css; charset=utf-8')
        if self.path=='/app.js': return self.static_asset('app.js','text/javascript; charset=utf-8')
        if self.path=='/theme.css': return self.static_asset('theme.css','text/css; charset=utf-8')
        if self.path=='/assets/strata-atmosphere.png': return self.static_asset('assets/strata-atmosphere.png','image/png')
        if self.path=='/assets/answerlayer-icon.png': return self.static_asset('assets/answerlayer-icon.png','image/png')
        if self.path=='/assets/answerlayer.ico': return self.static_asset('assets/answerlayer.ico','image/x-icon')
        if self.path=='/assets/answerlayer.icns': return self.static_asset('assets/answerlayer.icns','image/icns')
        if not self.authorized(): return self.reply(403,{'error':'Open this product through its launcher.'})
        if self.path=='/api/session':return self.reply(200,{'authenticated':True})
        if self.path=='/api/sample': return self.static_asset('sample.json','application/json; charset=utf-8')
        return self.reply(404,{'error':'Unknown resource'})
    def do_POST(self):
        if not self.authorized(): return self.reply(403,{'error':'Local session or origin mismatch'})
        if self.path=='/api/session':
            self.issue_session=True;return self.reply(200,{'authenticated':True})
        try:
            size=int(self.headers.get('Content-Length','0'))
            if size<1 or size>2_000_000: return self.reply(413,{'error':'Native JSON must be under 2 MB'})
            raw=self.rfile.read(size)
            if len(raw)!=size:return self.reply(400,{'error':'Incomplete request body'})
            native_text=raw.decode('utf-8')
            if self.path!='/api/validate': return self.reply(404,{'error':'No mutation endpoint exists'})
            errors=validate_record(native_text)
            try: data=strict(native_text);fmt=data.get('format') if isinstance(data,dict) else None
            except ValueError:fmt=None
            self.reply(200,{'valid':not errors,'errors':errors,'format':fmt,'sha256':hashlib.sha256(raw).hexdigest(),'scope':'Exact submitted UTF-8 text checked for structure, reference and supplied history integrity. No prior checkpoint was supplied; history completeness, factual truth, consent, adoption and publication are not authenticated.'})
        except (ValueError,OSError,subprocess.SubprocessError) as error: self.reply(400,{'error':str(error)})
def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--no-browser',action='store_true'); parser.add_argument('--port',type=int,default=CONFIG['port']); parser.add_argument('--check',action='store_true'); parser.add_argument('--serve',action='store_true',help=argparse.SUPPRESS); args=parser.parse_args()
    if args.check:
        errors=validate_record(guard(ROOT/'sample.json').read_text(encoding='utf-8-sig')); print(json.dumps({'product':CONFIG['id'],'sample_errors':errors})); return bool(errors)
    identity={'product':CONFIG['id'],'version':CONFIG['version'],'workspace':str(ROOT),'runtime_sha256':RUNTIME_SHA}
    return launch(Handler,args,identity,TOKEN,Path(__file__).resolve())
if __name__=='__main__': raise SystemExit(main())
