#!/usr/bin/env python3
import os
from bs4 import BeautifulSoup

def main():
    site_dir = os.path.join(os.getcwd(), 'site')
    problems = []
    for root, _, files in os.walk(site_dir):
        for f in files:
            if not f.endswith('.html'):
                continue
            path = os.path.join(root, f)
            rel_dir = os.path.relpath(root, site_dir)
            with open(path, 'r', encoding='utf-8') as fh:
                soup = BeautifulSoup(fh, 'html.parser')
            for a in soup.find_all('a', href=True):
                href = a['href'].strip()
                # ignore URL fragments when resolving file targets
                href = href.split('#', 1)[0].strip()
                if href.startswith('mailto:') or href.startswith('tel:'):
                    continue
                if href.startswith('http://') or href.startswith('https://'):
                    continue
                if href.startswith('#'):
                    continue
                if href.startswith('/'):
                    target = href.lstrip('/')
                else:
                    target = os.path.normpath(os.path.join(rel_dir, href))
                candidate_paths = []
                if target.endswith('/'):
                    candidate_paths.append(os.path.join(site_dir, target, 'index.html'))
                else:
                    candidate_paths.append(os.path.join(site_dir, target))
                    candidate_paths.append(os.path.join(site_dir, target + '.html'))
                    candidate_paths.append(os.path.join(site_dir, target, 'index.html'))
                if not any(os.path.exists(p) for p in candidate_paths):
                    problems.append((os.path.relpath(path, site_dir), href, candidate_paths))
    print(f'Checked site HTML files under {site_dir}')
    if problems:
        print('\nBroken internal links found:')
        for src, href, tried in problems:
            print(f'- On {src}: {href} -> tried:')
            for t in tried:
                print(f'    {os.path.relpath(t, site_dir)}')
    else:
        print('No broken internal links found')

if __name__ == '__main__':
    main()
