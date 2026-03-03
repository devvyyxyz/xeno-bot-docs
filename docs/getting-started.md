# Getting Started

This guide shows how to run the docs site locally and build the static site for deployment.

## Local preview

Install dependencies and run the local server:

```bash
python -m pip install -r requirements.txt
mkdocs serve
```

Open http://127.0.0.1:8000 in your browser.

## Build

```bash
mkdocs build
```

The built site will be in the `site/` directory.
