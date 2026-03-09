#!/usr/bin/env python3
"""Generate per-host backlinks fragments from local docs/ Markdown links.

Writes fragments to: docs/_generated/backlinks/<path_safe>.md

Usage:
  python3 scripts/generate_backlinks.py

This script scans all .md files under docs/ and records which pages link
to each host page. It is safe to run before `mkdocs build`.
"""
import os
import re

ROOT = os.path.abspath(os.path.dirname(__file__) + '/..')
DOCS_DIR = os.path.join(ROOT, 'docs')
OUT_DIR = os.path.join(DOCS_DIR, '_generated', 'backlinks')
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def resolve_link(link_url, src_relpath):
    if link_url.startswith(('http://', 'https://', 'mailto:')):
        return None
    link_url = link_url.split('#', 1)[0].split('?', 1)[0]
    if not link_url:
        return None
    if link_url.startswith('/'):
        rel = link_url.lstrip('/')
    else:
        src_dir = os.path.dirname(src_relpath)
        rel = os.path.normpath(os.path.join(src_dir, link_url)).replace('\\', '/')
    if rel.endswith('/'):
        rel = rel + 'index.md'
    if not rel.endswith('.md'):
        maybe = rel + '.md'
        if os.path.exists(os.path.join(DOCS_DIR, maybe)):
            rel = maybe
        else:
            rel = os.path.join(rel, 'index.md')
    return os.path.normpath(rel).replace('\\', '/')


def find_all_links():
    links = {}  # src_relpath -> list of (title, resolved_rel)
    for root, _, files in os.walk(DOCS_DIR):
        # Skip generated output to avoid self-referential entries and
        # erroneous image-based backlink artifacts.
        out_dir_abs = os.path.abspath(OUT_DIR)
        root_abs = os.path.abspath(root)
        if root_abs.startswith(out_dir_abs):
            continue
        for f in files:
            if not f.endswith('.md'):
                continue
            full = os.path.join(root, f)
            rel = os.path.relpath(full, DOCS_DIR).replace('\\', '/')
            try:
                text = open(full, encoding='utf-8').read()
            except Exception:
                continue
            for title, url in LINK_RE.findall(text):
                resolved = resolve_link(url, rel)
                if not resolved:
                    continue
                links.setdefault(resolved, []).append((title or rel, rel))
    return links


def write_fragments(backlinks):
    os.makedirs(OUT_DIR, exist_ok=True)
    for target, sources in backlinks.items():
        # produce a safe filename for the target (strip existing .md to avoid .md.md)
        safe = target.replace('/', '_').replace('..', '')
        if safe.endswith('.md'):
            safe = safe[:-3]
        out_path = os.path.join(OUT_DIR, safe + '.md')
        lines = []
        # unique by source
        seen = set()
        for title, src in sorted(sources, key=lambda x: x[0].lower()):
            if src in seen:
                continue
            seen.add(src)
            link = '/' + src
            if link.endswith('index.md'):
                link = link[:-len('index.md')]
            elif link.endswith('.md'):
                link = link[:-3]
            lines.append(f'- [{title}]({link})')
        if not lines:
            content = ''
        else:
            content = '\n'.join(lines) + '\n'
        with open(out_path, 'w', encoding='utf-8') as fh:
            fh.write(content)
        print('Wrote', out_path)


def main():
    backlinks = find_all_links()
    write_fragments(backlinks)


if __name__ == '__main__':
    main()
