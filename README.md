# Xeno Bot Docs (MkDocs)

This repository contains the documentation site for Xeno Bot using MkDocs + Material theme.

Local quickstart

```bash
python -m pip install -r requirements.txt
mkdocs serve
```

Build static site

```bash
mkdocs build
```

Deployment

The included GitHub Actions workflow will build the site on pushes to `main` and deploy to GitHub Pages.

Edit `mkdocs.yml` and `docs/` to add content.
