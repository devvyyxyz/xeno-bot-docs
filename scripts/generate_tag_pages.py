#!/usr/bin/env python3
import os
import re
import yaml
from pathlib import Path

DOCS_DIR = Path('docs')
TAGS_DIR = DOCS_DIR / 'tags'

def read_front_matter(path):
    text = path.read_text(encoding='utf-8')
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except Exception:
        return {}

def slugify(tag: str) -> str:
    s = tag.lower()
    s = re.sub(r'&', 'and', s)
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = s.strip('-')
    return s or tag

def main():
    tag_map = {}
    for root, _, files in os.walk(DOCS_DIR):
        for f in files:
            if not f.endswith('.md'):
                continue
            p = Path(root) / f
            if p.parts[0] == 'docs' and 'tags' in p.parts:
                continue
            meta = read_front_matter(p)
            tags = meta.get('tags') or []
            for t in tags:
                slug = slugify(str(t))
                tag_map.setdefault(slug, {'tag': t, 'pages': []})
                # compute doc path relative to docs/
                rel = os.path.relpath(p, DOCS_DIR)
                # link to the page without .md
                url = '/' + rel.replace(' ', '%20').rsplit('.md', 1)[0]
                tag_map[slug]['pages'].append((p.name.replace('.md',''), url))

    TAGS_DIR.mkdir(parents=True, exist_ok=True)
    for slug, info in tag_map.items():
        out = TAGS_DIR / slug / 'index.md'
        out.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            f'---',
            f'title: {info["tag"]}',
            f'permalink: /tags/{slug}/',
            f'toc: false',
            "hide: ['navigation']",
            f'---',
            f'\n# Pages tagged "{info["tag"]}"\n'
        ]
        for name, url in sorted(info['pages']):
            lines.append(f'- [{name}]({url})')
        out.write_text('\n'.join(lines), encoding='utf-8')
    print(f'Generated {len(tag_map)} tag pages under {TAGS_DIR}')

if __name__ == '__main__':
    main()
