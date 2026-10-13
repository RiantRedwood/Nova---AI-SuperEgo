# AnswerLayer 0.3.1

Release 0.3.1 carries the accepted inspector and ledger repairs forward. Native v2 records retain product_version 0.3.0, so existing saved records remain compatible.

Decide whether new evidence changes an answer you already rely on, then preserve exactly what changed and why. Start in conversation with your current answer, its known date/scope, the new material and the decision you need to make. A short comparison can stay short.

## Try a complete local example

Python 3.10 or newer is required for the optional tools; they use only the standard library. From this skill folder, follow [Your first local patch](examples/first-value/README.md). It produces a new checkpoint while preserving the original, then checks history and writes a local brief. The evidence and recorded authorization in that example are fictional.

For a visual comparison, follow the [Answer Change Desk guide](workspace/README.md). For your own continuing work, use the [native operations reference](knowledge/native-ledger-reference.md). For older records, follow [v1 migration](examples/legacy-v1/README.md). Without local tools, use the [conversation workflow](fallbacks/universal-copy-paste-workflow.md).

## Know what is stored

Your files stay in the location you choose. The browser holds a transient copy, and its launcher retains same-user reconnect metadata in the OS temporary directory. No case store, remote service, automatic monitor or publisher is created. Preserve original checkpoints and confirm downloaded files before closing the desk. See [Recovery and limits](knowledge/native-ledger-reference.md).
