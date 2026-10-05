# Site shell (Docsify)

This directory holds **site-only** pages and notes. Canonical messaging stays in `framework/`, `products/`, `offerings/`, and the other paths listed in the root `_sidebar.md`.

## How publishing works

- **Published from the `gh-pages` branch.** [`pages-deploy.yml`](../.github/workflows/pages-deploy.yml) copies the `main` branch to the root of `gh-pages` on every push to `main`.
- **PR previews.** [`pages-pr-preview.yml`](../.github/workflows/pages-pr-preview.yml) publishes each pull request to `https://percona.github.io/percona-messaging/pr-preview/pr-<number>/` and posts the link as a PR comment. The preview updates on each push and is removed when the PR closes. PRs from forks do not get a preview.
- **No markdown reformat.** Docsify renders existing `.md` files in place.
- After merge to `main`, Pages updates automatically (may take a minute or two).
- **Not indexed by search engines.** `index.html` includes `noindex`, and `robots.txt` disallows crawlers. Share the URL directly; do not rely on organic search.

## Files that power the site

| File | Role |
| --- | --- |
| `/index.html` | Docsify entry point |
| `/.nojekyll` | Tells GitHub Pages not to run Jekyll |
| `/_sidebar.md` | Reader navigation |
| `/site/home.md` | Landing page copy |
| `/site/how-this-works.md` | Intro before the playbook |

## Local preview

From the repository root:

```bash
python3 -m http.server 8080
```

Open `http://localhost:8080/` in a browser.

## Updating navigation

When you add a new canonical page, link it from the nearest folder `README.md` (existing repo habit), then add an entry to `/_sidebar.md`.

## Enable GitHub Pages (one-time)

Repository **Settings → Pages**:

- Source: **Deploy from a branch**
- Branch: **`gh-pages`**, folder **`/ (root)`** (the branch is created by the first run of `pages-deploy.yml`)
- Save. The site URL will be `https://percona.github.io/percona-messaging/`
