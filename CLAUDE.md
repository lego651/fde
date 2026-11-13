# FDE repo rules

- **Every client document goes on the Pages site.** Follow the `fde-docs` skill (`.claude/skills/fde-docs/SKILL.md`): write the file into `<Client>/`, register it in `<Client>/docs.json`, run `python3 scripts/build_docs.py <Client>`, push `main`, verify the live URL. Artifacts and scratchpad files are previews only.
- Never edit `<Client>/docs.html` or the `DOCSTRIP` block in `<Client>/index.html` by hand; they are generated.
- Root `*-preview.html` files are design previews; don't commit them.
- `scripts/stop_check.sh` runs as a Stop hook and blocks finishing while the doc center is out of sync. Fix the cause; don't work around it.
