# Answer Change Desk

Inspect the current answer beside an exact proposal and its referenced evidence. Edit or download a working copy while the original file stays untouched. Strata and Switchyard offer two dark themes around the same record.

## Open the desk

Install the complete skill folder and use Python 3.10+. No pip dependencies are required. On Windows, open `Open.cmd` in this folder. On macOS/Linux, run `python3 -B host.py` from this folder, or make `Open.command` executable and run it. The launcher opens a private loopback browser session. Reopening the same current runtime can reconnect to its existing server. To see startup errors, run `python -B host.py --no-browser` and use its printed session URL privately.

1. Choose **Example** for the labeled fictional delivery case, or **Open an answer record** for your own v1/v2 native JSON file.
2. Read **Current answer** and select a proposed change. **Proposed wording** returns to that same comparison view. The patch search filters by recorded text; select the matching patch to see exact referenced source IDs.
3. Use **Changes & exclusions**, **Evidence** and **Recheck triggers** to inspect the recorded reasoning. **Recorded review decisions**, **Publication fields** and **Retained prior answers** expand details; their presence is not proof of consent, publication or complete history.
4. Choose **Edit working file** to edit the complete native JSON. **Use working copy** replaces only page memory. Malformed drafts remain open with an error. **Cancel** or Escape asks before discarding an unapplied changed draft.
5. Choose **Validate**. The result includes the submitted text hash. If you edit while a request is running, the result is marked **STALE** and cannot certify the new text. v1 receives a legacy-readability result, not current approval eligibility. No earlier checkpoint is supplied by this browser check.
6. Choose **Download working file**, confirm the file exists in your browser's download destination, and reopen that file when resuming. Compare an important edit before closing. A requested download cannot be confirmed by the page, so edits keep the leave-page warning even after a successful download. A canceled download keeps that warning too.

## Change the theme and return

Use **Workspace** to choose **Strata · dark** or **Switchyard · enamel**. Navigation buttons return to the current record without saving or adopting it. Controls have visible text/labels and can be reached with keyboard Tab; dialogs use native browser focus handling. Actual Windows Chromium checks cover the documented core flow; screen-reader conformance and macOS/Linux launch have not been established.

## Recover without losing work

A failed import or failed Example request retains the prior working copy. Duplicate JSON keys, nonfinite literals, over 2 MB input, excessive nesting and unsupported formats are refused. Correct the source on a copy and retry. Changed drafts and edited working copies trigger replacement/leave warnings; confirm discarding only when you have the copy you need. Browser crashes and forced termination can still lose unsaved memory. There is no localStorage, autosave or hidden record store.

Large numeric literals and unknown fields display without floating-point rounding; downloads retain the exact imported or entered JSON text. Structural repair is explicit: malformed native collections display an explanation and remain editable/downloadable when the top-level format can be parsed. **Validate** may reject a record the inspector can display. Inspection is not adoption.

If a session is missing, relaunch from `Open.cmd`/`Open.command`; keep the URL fragment token private. If a port is occupied, the launcher can choose another and prints the actual URL. If the runtime is stored through a symbolic link/junction, move an ordinary complete copy to a normal folder and launch it. Same-user reconnect metadata lives under the OS temporary `cd-native-desks` folder and contains a local token; it is not a case store. Do not serve this desk on a public network.

For actual adoption to a new checkpoint, use [native operations](../knowledge/native-ledger-reference.md). A browser edit, validation or download does not apply a patch, publish a brief or schedule a watch.

## Maintainer browser check

`node workspace/test_workbench.cjs SKILL_ROOT OUTPUT_DIRECTORY` runs actual Chromium interactions against an isolated local host. It requires Node, Playwright and Chromium supplied by the test environment. `PYTHON`, `PLAYWRIGHT_MODULE` and `CHROMIUM_PATH` can select installed runtimes; no test downloads or installation occur. Results and an actual screenshot are written to the chosen output directory. These test dependencies are not required to use the desk.


## Create an optional product entry

Keep the complete installed runtime in its intended location. You need Python 3.10 or newer and an existing writable folder where you want the entry. Creation preserves an existing AnswerLayer entry and does not open the desk automatically.

From the installed skill folder on Windows, run:

```text
python -B workspace/create_entry.py --directory "C:\My Entries"
```

Replace the example with your chosen existing folder. A successful result says `created` and names `AnswerLayer.lnk`; opening that shortcut starts the existing Answer Change Desk with the product icon.

On macOS, run:

```text
python3 -B workspace/create_entry.py --platform mac --directory "/Users/me/My Entries"
```

A successful result names `AnswerLayer.app`. It contains the product ICNS icon and follows the same Python launch chain. Native macOS launch remains untested until exercised on a Mac; construction on Windows is portable-package evidence only.

If creation says `refused`, retain the named error. Check that your selected folder exists and is writable, and choose another folder when an AnswerLayer entry already exists. Keep the complete runtime together and in place; recreate your entry after moving it. To remove an entry, delete only the exact shortcut or app bundle you created. Your runtime and saved answer files remain separate. The existing `Open.cmd`/`Open.command` launchers remain available.
