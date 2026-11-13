---
name: fde-docs
description: Publish every FDE client deliverable (analysis, plan, report, poster, form, research write-up, comparison, design preview the user approved) to the client's doc center on GitHub Pages (https://lego651.github.io/fde/<client>/). Use whenever you create or change a document for an FDE client such as VHealth / V-Health Rehab Clinic, whenever the user says 放到 pages / 文档中心 / doc center / push 上去 / 更新文档 / work in progress doc, or when a doc's status changes (分析中 → 已完成). Also use before replying "done" on any VHealth or FDE task that produced a file.
---

# FDE doc center

Repo: `/Users/jason/TEMP/fde` → GitHub `lego651/fde`, branch `main`, GitHub Pages (Jekyll).
Each client has a folder (e.g. `VHealth/`) with:

| File | What it is | Edit how |
|---|---|---|
| `<Client>/docs.json` | **The registry.** Every doc: category, title, type, date, status, path | By hand |
| `<Client>/deliverables/` | HTML / PDF deliverables | Write files here |
| `<Client>/*.md` | Markdown docs (Jekyll renders `x.md` → `x.html`) | Write files here |
| `<Client>/index.html` | Timeline page `/<slug>/`. Top strip is **generated** between `DOCSTRIP` markers | Timeline events by hand; never touch the strip |
| `<Client>/docs.html` | "See all" page `/<slug>/docs/` | **Generated**, never edit |
| `scripts/build_docs.py` | Builds strip + docs page; `--check` validates | Run it |
| `scripts/stop_check.sh` | Stop hook that refuses to finish while anything is unpublished | Don't bypass |

## The rule

**A client document is not done until it is in the repo, registered in `docs.json`, built, pushed to `main`, and live.**
Artifacts (claude.ai) and scratchpad files are previews only. The Pages site is the source of truth.

## Steps (every time)

1. **Write the file into the repo**, not the scratchpad:
   - HTML/PDF → `<Client>/deliverables/<kebab-name>.html|pdf`
   - Markdown → `<Client>/<kebab-name>.md` (plain markdown; Jekyll renders it to `.html`).
   - Use the paper palette already used by the site (`--paper #fbf8f2`, `--accent #c9772e`, serif headings Noto Serif SC).
2. **Register it in `<Client>/docs.json`** → add to `docs`:
   ```json
   { "cat": "grow", "title": "中文标题", "type": "HTML", "date": "YYYY-MM-DD", "status": "wip", "path": "deliverables/x.html", "featured": true }
   ```
   - `cat`: a key from `categories` (add a new category with a distinct colour only if none fits).
   - `type`: `HTML` | `PDF` | `MD`. For MD, `path` is the **.html** served name (`plan-90-day.html`).
   - `status`: `wip` 分析中 (still being discussed/decided) · `use` 使用中 (a live tool, e.g. a form) · `done` 已完成.
   - `featured: true` keeps a non-wip doc in the homepage strip. wip docs are always in the strip.
   - Source files that only exist to produce a PDF go in `ignore` with a reason.
   - Updating an existing doc: change its `status` / `date` / `title` here; add a dated "补充（MM/DD）" section inside the doc rather than silently rewriting conclusions.
3. **Build:** `python3 scripts/build_docs.py <Client>` then `python3 scripts/build_docs.py --all --check` (must print `doc center OK`).
4. **Timeline (if this is a new decision or milestone):** add or update the event in `<Client>/index.html` (description, deliverables links, next actions) and the "现在要做的事" card counts. Not needed for small updates to an existing doc.
5. **Commit and push `main`** — only the client folder / scripts / skill files, never the root `*-preview.html` scratch files. End the message with the Co-Authored-By line.
6. **Verify live:** wait for `gh api repos/lego651/fde/pages/builds/latest` to show `built <sha>`, then `curl` the doc URL, `/<slug>/` and `/<slug>/docs/` → all 200.
7. **Reply** with the live URL `https://lego651.github.io/fde/<Client>/<path>` (not the artifact link).

## Exceptions

- The user is choosing between design options ("先给我看3个方案") → preview HTML at the repo root (`*-preview.html`, not committed) or an artifact. Publish only the chosen version.
- The user explicitly says not to push yet → don't push; say clearly which docs are unpublished.

## New client

Create `<Client>/` with `index.html` (copy VHealth's structure, `permalink: /<slug>/`), `assets/logo.*`, and `docs.json`; add a card to the root `index.html`; run the build — it inserts the strip after `</header>` on first run.
