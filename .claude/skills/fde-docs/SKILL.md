---
name: fde-docs
description: Publish every FDE client deliverable (analysis, plan, report, poster, form, research write-up, comparison, approved design) to that client's doc center on GitHub Pages (https://lego651.github.io/fde/<slug>/), and set up new FDE clients. Use whenever you create or change a document for any FDE client (currently VHealth / V-Health Rehab Clinic; more will be added), when the user says 放到 pages / 文档中心 / doc center / push 上去 / 更新文档 / 新客户 / add a client, when a doc's status changes (分析中 → 已完成), and before replying "done" on any FDE client task that produced a file.
---

# FDE doc center

Repo `/Users/jason/TEMP/fde` → GitHub `lego651/fde`, branch `main`, GitHub Pages (Jekyll). **The repo and site are public.**

## Clients are separate

Each client is one top-level folder with its own `docs.json`. List them with `ls /Users/jason/TEMP/fde/*/docs.json`.

| Folder | Slug (URL) | Client |
|---|---|---|
| `VHealth/` | `/fde/vhealth/` | V-Health Rehab Clinic, Calgary NW |

(Read `client.slug` / `client.name` in each `docs.json` for the current list; add a row here when you add a client.)

1. **Work out which client the doc belongs to before writing anything.** Use the conversation (business name, what was discussed). If it could be more than one client, or it's a new business not in the list, ask the user. Never guess.
2. A client's files live only in its own folder, are registered only in its own `docs.json`, and link only within that folder. No cross-client links or shared deliverables unless the user asks.
3. Categories are per client (`categories` in that client's `docs.json`). Don't copy another client's categories just because they exist.
4. One commit per client when a session touched several.
5. Public site: no personal data of the client's customers (names, phones, filled-in forms, health info). Business-level facts the owner shared are fine.

## Per-client files

| File | What | Edit how |
|---|---|---|
| `<Client>/docs.json` | **Registry**: client info, categories, every doc | By hand |
| `<Client>/deliverables/` | HTML / PDF deliverables | Write files here |
| `<Client>/*.md` | Markdown docs (Jekyll renders `x.md` → `x.html`) | Write files here |
| `<Client>/index.html` | Timeline page `/<slug>/` | Timeline by hand; the `DOCSTRIP` block is **generated** |
| `<Client>/docs.html` | "See all" page `/<slug>/docs/` | **Generated**, never edit |

Shared: `scripts/build_docs.py` (build / `--check`), `scripts/new_client.py` (scaffold), `scripts/stop_check.sh` (Stop hook).

## The rule

**A client document is not done until it is in the client's folder, registered in that client's `docs.json`, built, pushed to `main`, and live.** Artifacts (claude.ai) and scratchpad files are previews only.

## Steps: new or changed document

1. **Write the file into the client folder**, not the scratchpad:
   HTML/PDF → `<Client>/deliverables/<kebab-name>.html|pdf`; Markdown → `<Client>/<kebab-name>.md`.
   Match the site's paper palette (`--paper #fbf8f2`, `--accent #c9772e`, Noto Serif SC headings).
2. **Register it in `<Client>/docs.json`** under `docs`:
   ```json
   { "cat": "grow", "title": "中文标题", "type": "HTML", "date": "YYYY-MM-DD", "status": "wip", "path": "deliverables/x.html", "featured": true }
   ```
   - `cat`: a key from this client's `categories` (add one with a distinct colour only if none fits).
   - `type`: `HTML` | `PDF` | `MD`. For MD, `path` is the served `.html` name.
   - `status`: `wip` 分析中 · `use` 使用中 (a live tool such as a form) · `done` 已完成.
   - `featured: true` keeps a non-wip doc in the homepage strip; wip docs are always shown.
   - Files that only exist to produce a PDF go in `ignore` with a reason.
   - Changing a doc: update `status` / `date` here; add a dated "补充（MM/DD）" section inside the doc rather than silently rewriting earlier conclusions.
3. **Build:** `python3 scripts/build_docs.py <Client>`, then `python3 scripts/build_docs.py --all --check` → must print `doc center OK`.
4. **Timeline (new decision or milestone only):** add/update the event in `<Client>/index.html` (description, deliverable links, next actions) and the "现在要做的事" card if the client has one.
5. **Commit and push `main`**: only that client's folder (plus scripts/skill if changed). Never commit root `*-preview.html`. End with the Co-Authored-By line.
6. **Verify live:** wait until `gh api repos/lego651/fde/pages/builds/latest --jq .status` is `built` for your commit; `curl` the doc URL, `/<slug>/`, `/<slug>/docs/` → 200.
7. **Reply** with the live URL `https://lego651.github.io/fde/<Client>/<path>`.

## Steps: new client

1. Confirm with the user: display name, folder name (CamelCase, e.g. `AcmeDental`), slug (lowercase, e.g. `acme`), one-line subtitle, logo (file or URL; download into the scratchpad first).
2. `python3 scripts/new_client.py --folder <Folder> --slug <slug> --name "<Name>" --subtitle "<line>" [--logo <path>]`
   It creates `<Folder>/docs.json`, `<Folder>/index.html` (empty timeline + doc strip), the logo, and a card on the root page, then builds.
3. Adjust `categories` in the new `docs.json` to fit this business; add the client to the table above.
4. Commit, push, verify `/fde/<slug>/` and `/fde/<slug>/docs/` → 200.

## Exceptions

- The user is choosing between options ("先给我看3个方案") → preview at the repo root as `*-preview.html` (excluded from the site, not committed) or as an artifact. Publish only what they choose.
- The user explicitly says not to push yet → don't; say which docs are unpublished.

## Enforcement

`scripts/stop_check.sh` runs as a Claude Code Stop hook (in `~/.claude/settings.json`). In any session that touched this repo, it refuses to let Claude finish while a client folder has unregistered files, stale generated pages, uncommitted changes, or unpushed commits. Fix the cause; don't work around it.
