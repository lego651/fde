# FDE repo rules

- **Multiple clients, kept separate.** Each client is one folder with its own `docs.json` (`ls */docs.json`). Decide which client a document belongs to before writing it; if unclear or new, ask. Never put one client's files, links or docs.json entries in another client's folder.
- **Every client document goes on the Pages site.** Follow the `fde-docs` skill (`.claude/skills/fde-docs/SKILL.md`): file in `<Client>/`, entry in `<Client>/docs.json`, `python3 scripts/build_docs.py <Client>`, push `main`, verify the live URL. Artifacts and scratchpad files are previews only.
- **New client:** `python3 scripts/new_client.py --folder <Folder> --slug <slug> --name "<Name>" --subtitle "<line>" [--logo <path>]`, then adjust its categories.
- Never edit `<Client>/docs.html` or the `DOCSTRIP` block in `<Client>/index.html` by hand; they are generated.
- The site is public: no personal data about a client's customers.
- Root `*-preview.html` files are design previews; don't commit them.
- `scripts/stop_check.sh` runs as a Stop hook and blocks finishing while the doc center is out of sync. Fix the cause; don't work around it.
