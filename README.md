# Scando-lab — multipage Quarto website

A contribution-friendly Quarto adaptation of
[Scando-lab](https://michelescandola.github.io/scando-lab/), retaining the
original visual identity and research content.

The website has a homepage and seven separate sections:

| Page | Source |
| --- | --- |
| Home | `index.qmd` |
| Research | `research.qmd` |
| Open Science | `open-science.qmd` |
| People | `people.qmd` |
| Activities | `activities.qmd` |
| Publications | `publications.qmd` |
| Resources | `resources.qmd` |
| Contact | `contact.qmd` |

## Preview and render

Install [Quarto](https://quarto.org/docs/get-started/), version 1.6 or newer.
The build was verified with **Quarto 1.11.9**. No R, Python, Node.js or additional
packages are needed to render the website.

From the project directory:

```sh
quarto preview
```

To render all pages:

```sh
quarto render
```

The rendered website is in `_site/`. Open `_site/index.html` in a browser or
serve that directory with any static web server. In the supplied download,
the rendered pages are already included.

## Make a contribution

Page prose is Markdown. Repeated content is kept in ordinary YAML lists under
`content/` and displayed with Quarto's native listing system:

- `research.yml`: research themes.
- `people.yml`: team profiles and portrait links.
- `activities.yml`: announcements, talks, workshops and events.
- `publications.yml`: publication metadata and filter categories.
- `resources.yml`: resource descriptions and links.

Contributors can edit these files directly in GitHub and propose a pull
request. See [CONTRIBUTING.md](CONTRIBUTING.md) for copyable examples.
Shared templates keep the appearance consistent without requiring
contributors to write layout HTML.

The Activities list starts empty because the original website did not supply
event announcements or dates. Its empty state updates automatically when a
real activity is added. Resources currently point to the reproducibility
network, methods preprints and bibliography already referenced by the source.

## Checks

The GitHub Actions workflow in `.github/workflows/render.yml` renders the
site and validates local links, assets, IDs and heading counts on pull
requests and pushes to `main`.

To run the same local validation, using Python's standard library:

```sh
python3 scripts/check_site.py
```

The shared navigation highlights the current page and collapses into a menu
on small screens. Publication filters show all eight selected works or the
four entries in either category. Motion preferences are respected.

## Repository and hosting

The project is ready to place at the root of a GitHub repository. Its workflow
checks contributions and does not deploy the site. To host it, upload the
contents of `_site/` to a static host, or follow Quarto's
[GitHub Pages guide](https://quarto.org/docs/publishing/github-pages.html).
All page and asset links are relative and support project subdirectories.

## Attribution

The original site is MIT-licensed. Its copyright notice and license are
retained in `LICENSE`. The original source inspected on 10 November 2026 was
`michelescandola/scando-lab`, commit
`cc6841abc344eba04f981837a056baf20de10a62`.

Portraits retain transparency and were resized for web use. The two student
profiles with no source URL omit the profile link until a URL is supplied.
