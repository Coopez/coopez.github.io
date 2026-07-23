# CLAUDE.md

Personal academic website for Niklas Erdmann (PhD candidate, University of Oslo):
research, publications, talks, teaching, CV, and eventually a blog.

## Stack

[academicpages](https://github.com/academicpages/academicpages.github.io) — a
Jekyll template forked from Minimal Mistakes, adopted from the upstream repo and
stripped of demo content. Deploys via the **native GitHub Pages branch build
(no GitHub Actions)**: every gem in the Gemfile is Pages-whitelisted, so pushing
to `main` rebuilds the live site. Don't add a deploy workflow or introduce
plugins outside the Pages allow-list — that would force a CI pipeline.

## Structure

```
_pages/about.md          home page (permalink: /)
_pages/cv.md             CV page — auto-pulls the collections below + links files/cv.pdf
_pages/{publications,talks,teaching}.html   auto-generated list pages
_publications/*.md       one file per paper (see conventions)
_talks/*.md              one file per talk/poster
_teaching/*.md           one file per teaching role
_data/navigation.yml     top nav order
_config.yml              site + author sidebar config
files/                   user PDFs, served at /files/... (cv.pdf, talks/*.pdf)
images/                  images incl. profile.jpg (sidebar avatar)
cv/                      LaTeX source for the CV PDF (excluded from build)
_layouts _includes _sass assets   theme internals — rarely touched
```

## Adding content

- **A publication:** new `_publications/YYYY-MM-DD-slug.md`. Front matter:
  `title`, `collection: publications`, `category:` (one of `manuscripts` =
  journal, `conferences`, `preprints`), `permalink: /publication/slug`, `date`,
  `venue`, optional `paperurl` / `slidesurl`, and a `citation` (HTML allowed).
  Extra links (code, arXiv, DOI) go in the body as Markdown.
- **A talk:** new `_talks/YYYY-MM-DD-slug.md`. Front matter: `title`,
  `collection: talks`, `type`, `permalink: /talks/slug`, `venue`, `date`,
  `location`. Slides/poster links go in the body.
- **A teaching entry:** `_teaching/*.md`, `collection: teaching`, same shape.
- **A blog post:** `_posts/YYYY-MM-DD-slug.md` — the blog (`/year-archive/`) is
  intentionally empty for now; it grows as posts are added.
- Filename date drives sort order; the `permalink` is the public URL. Individual
  pages render at `/publication/slug.html` and `/talks/slug.html`.

## Conventions

- Asset links are root-relative: `/files/cv.pdf`, `/images/foo.jpg`. They work
  regardless of the final site URL.
- Content is the user's — never invent publications, dates, venues, or bio
  facts. Leave an HTML comment `<!-- TODO: ... -->` (invisible on the page) and
  say so, rather than visible "TODO" text.

## Deliberately removed from upstream academicpages

Portfolio collection, the `markdown_generator/` TSV import scripts (see the
`academicpages-generators-deferred` memory + TODO.md — revisit at ~20–30 pubs),
the talkmap feature, and the upstream `.github/` CI. Don't reintroduce without a
reason.

## Working on this repo

- Preview: `.\serve.ps1` → <http://localhost:4000> (Docker Desktop must be
  running; no Ruby install needed). It **builds then serves the static `_site/`
  with webrick** — deliberately NOT `jekyll serve`, which on Windows rewrites the
  url to `http://0.0.0.0:4000` and leaves the page unstyled (browsers can't load
  assets from 0.0.0.0). Don't "simplify" it back to `jekyll serve`. The build
  uses `_config_docker.yml` (`url:""`) so asset links are root-relative.
- Run the Docker commands from the **PowerShell tool**, not the Bash tool —
  git-bash mangles the `-w /site` container path.
