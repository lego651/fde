#!/usr/bin/env python3
"""Scaffold a new FDE client.

  python3 scripts/new_client.py --folder Acme --slug acme --name "Acme" \
      --subtitle "Acme Dental · Calgary SW" [--logo /path/to/logo.png]

Creates:
  <Folder>/docs.json        empty registry with default categories
  <Folder>/index.html       timeline page at /<slug>/ (same look as VHealth), doc strip included
  <Folder>/assets/logo.*    if --logo is given
  a card in the root index.html (above <!-- CLIENT-CARDS:END -->)
Then runs build_docs.py for the new folder.
"""
import argparse, html, json, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / 'VHealth' / 'index.html'   # source of the shared CSS only
DEFAULT_CATS = [
    {'key': 'diag', 'name': '诊断 & 访谈', 'color': '#c9772e'},
    {'key': 'plan', 'name': '计划 & OKR', 'color': '#10715f'},
    {'key': 'grow', 'name': '增长分析', 'color': '#4b3fb5'},
    {'key': 'ops', 'name': '运营工具', 'color': '#1d5fa8'},
    {'key': 'design', 'name': '设计物料', 'color': '#b84a62'},
]
e = html.escape


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--folder', required=True, help='Folder name, e.g. Acme (CamelCase, no spaces)')
    ap.add_argument('--slug', required=True, help='URL slug, e.g. acme -> /fde/acme/')
    ap.add_argument('--name', required=True, help='Display name')
    ap.add_argument('--subtitle', default='', help='One line under the title')
    ap.add_argument('--logo', help='Path to a logo image')
    a = ap.parse_args()

    if not re.fullmatch(r'[A-Za-z0-9-]+', a.folder) or not re.fullmatch(r'[a-z0-9-]+', a.slug):
        sys.exit('folder: letters/digits/-; slug: lowercase letters/digits/-')
    folder = ROOT / a.folder
    if folder.exists():
        sys.exit(f'{folder} already exists')
    taken = {json.loads(p.read_text(encoding='utf-8'))['client']['slug'] for p in ROOT.glob('*/docs.json')}
    if a.slug in taken:
        sys.exit(f'slug "{a.slug}" is already used by another client')

    (folder / 'deliverables').mkdir(parents=True)
    (folder / 'deliverables' / '.gitkeep').write_text('')
    logo_rel = ''
    if a.logo:
        src = Path(a.logo).expanduser()
        (folder / 'assets').mkdir()
        logo_rel = f'assets/logo{src.suffix.lower()}'
        shutil.copy(src, folder / logo_rel)

    (folder / 'docs.json').write_text(json.dumps({
        'client': {'slug': a.slug, 'name': a.name, 'logo': logo_rel, 'logo_alt': f'{a.name} logo'},
        'categories': DEFAULT_CATS, 'docs': [], 'ignore': {},
    }, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    css = re.search(r'<style>.*?</style>', TEMPLATE.read_text(encoding='utf-8'), re.S).group(0)
    css = re.sub(r'\n?/\* DOCSTRIP-CSS:START.*?DOCSTRIP-CSS:END \*/', '', css, flags=re.S)
    logo_html = (f'<span class="logo-plate"><img src="../{a.folder}/{logo_rel}" alt="{e(a.name)} logo"></span>'
                 if logo_rel else '')
    (folder / 'index.html').write_text(f'''---
layout: null
permalink: /{a.slug}/
---
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(a.name)} 项目时间线</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;600;700;800&family=Noto+Sans+SC:wght@400;500;700&family=Noto+Serif+SC:wght@600;700&display=swap" rel="stylesheet">
{css}
</head>
<body>
<main>
  <a class="back" href="../">← 所有客户</a>

  <header class="hd">
    {logo_html}
    <div>
      <h1>{e(a.name)} 项目时间线</h1>
      <p>{e(a.subtitle)}</p>
    </div>
  </header>

  <h2 class="sec">时间线</h2>
  <ol class="timeline">
    <li class="ev next">
      <div class="top"><h3>第一个事件</h3><span class="date">待定</span></div>
      <p style="margin:0;color:var(--muted)">诊断访谈之后在这里记录。</p>
    </li>
  </ol>
</main>
</body>
</html>
''', encoding='utf-8')

    root = ROOT / 'index.html'
    s = root.read_text(encoding='utf-8')
    marker = '    <!-- CLIENT-CARDS:END'
    if marker not in s:
        sys.exit('root index.html has no CLIENT-CARDS:END marker')
    logo_card = (f'<div class="logo"><img src="{a.folder}/{logo_rel}" alt="{e(a.name)} logo"></div>'
                 if logo_rel else f'<div class="logo" style="min-height:90px;font-weight:800;font-size:1.4rem;color:#17262b">{e(a.name)}</div>')
    card = f'''    <a class="client" href="{a.slug}/">
      {logo_card}
      <div>
        <div class="name">{e(a.name)}</div>
        <div class="meta">{e(a.subtitle)}</div>
      </div>
      <span class="go">查看项目 →</span>
    </a>
'''
    root.write_text(s.replace(marker, card + marker, 1), encoding='utf-8')

    subprocess.run([sys.executable, str(ROOT / 'scripts' / 'build_docs.py'), a.folder], check=True)
    print(f'\nCreated {a.folder}/  →  https://lego651.github.io/fde/{a.slug}/')
    print('Next: commit + push main (see the fde-docs skill).')


if __name__ == '__main__':
    main()
