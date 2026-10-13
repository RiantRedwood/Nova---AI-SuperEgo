# Beryl IT Studio 0.4.0

Run `python -B host.py` from this workspace folder with Python 3.10+, or use Open.cmd on Windows / Open.command on macOS or Linux. No pip dependencies are required. Reopening the launcher reconnects a matching private instance; it cannot restore a closed tab's memory. See [the skill quick start](../docs/QUICK-START.md).

Select **Start a case** to enter your own device, symptom and desired outcome. Unknown authority and risk remain unknown; this creates an incomplete record, never a diagnosis. **Open case** imports a native JSON; **Explore example** is a labeled synthetic case. Investigation compares recorded explanations, selected test, provenance and result. Evidence and Recovery & proof expose the retained basis. Old state/value/test fields stay visible and conflicting aliases are flagged without rewriting the original file.

**Record observed result** requires explicit performed confirmation, an actual observation, evidence kind and named source. Choose rerun/new observation or transcription correction. Earlier recorded results remain in result_history. A changed observation marks prior verification for reassessment and an imported review stale. **Edit case JSON** retains unknown fields but is an advanced editor; preserve previous evidence when reconciling facts. **Check structure** also reports bounded declared-consistency issues. Neither it nor the case file proves physical work, permission or repair.

**IT review** displays a supplied JSON, Markdown or text artifact. JSON case_id/reviewed_case_id and case_updated_at declarations are checked against the selected record when present. Matching strings do not authenticate independence; missing binding is unknown. Retain the original review separately.

**Download copy** requests a native file. Confirm it reached your files before closing/reloading. Working state is only in this tab; there is no durable owner store, browser database, automatic save or device-command endpoint. Failed import retains the previous case. An unavailable host still permits local editing/download; example loading and checks need the host.

The private service uses loopback, exact host/origin checks and an HttpOnly SameSite=Strict cookie. Duplicate launch compares product/version/workspace/runtime bytes and process nonce; health contains no session token. Temporary same-user launch metadata is disposable, not case storage. Do not share the credential-bearing startup URL. Windows normal launch hides its background helper; `--no-browser --port 0` is a foreground diagnostic mode.

Mossglass, Night Probe and Cinder Relay preserve data while changing the environment. Native controls, dialogs and a skip link support keyboard use; this is not a conformance or participant-usability claim. Run `python -B host.py --check` for the synthetic sample, or `python -B -m unittest discover -v` here for retained local host/schema checks. The [case guide](../docs/CASE-FILES.md) explains standalone validator commands and closure records.

## Optional desktop entry

The Studio can keep a product entry in an existing folder you choose. From the installed `beryl-it-tech` folder, run `python -B workspace/create_entry.py --directory "<existing folder>"`. Windows creates `Beryl IT Studio.lnk`; macOS creates `Beryl IT Studio.app`. Open that entry to use the existing Studio launch chain. It opens no device connection and saves no case automatically.

The helper refuses to replace an existing same-named entry. Remove only your known old entry if you intentionally want to recreate it. Keep the installed skill in place: moving or deleting it breaks the entry; recreate the entry against its new location. Python remains required. Mac bundle construction is portable; native Mac launch is not claimed.
