# Scando-lab — multipage Quarto website

A contribution-friendly Quarto adaptation of
[Scando-lab](https://michelescandola.github.io/scando-lab/), retaining the
original visual identity and research content.

Website: <https://michelescandola.github.io/scando-lab-quarto-preview/>

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

The **Build and deploy Quarto** workflow in `.github/workflows/render.yml`
renders the site and validates local links, assets, IDs and heading counts
on pull requests and pushes to `main`. After successful checks, pushes to
`main` automatically publish the rendered site to GitHub Pages. Pull requests
run the checks without deploying.

To run the same local validation, using Python's standard library:

```sh
python3 scripts/check_site.py
```

The shared navigation highlights the current page and collapses into a menu
on small screens. Publication filters show all eight selected works or the
four entries in either category. Motion preferences are respected.

## Repository and hosting

The source is hosted at
<https://github.com/michelescandola/scando-lab-quarto-preview>.
GitHub Pages publishes the `_site/` artifact built by the workflow, using the
`github-pages` deployment environment. Quarto sources and content lists stay
on `main`; generated HTML does not need to be committed.

To republish without changing content, open the repository's **Actions** tab,
select **Build and deploy Quarto**, and choose **Run workflow** on `main`.
The workflow has no deployment step for pull requests.

The public base URL is set in `_quarto.yml` under `website.site-url`. Update
that value if the repository name or hosting domain changes. Page and asset
links are relative and support the GitHub Pages project subdirectory.

## Attribution

The original site is MIT-licensed. Its copyright notice and license are
retained in `LICENSE`. The original source inspected on 10 November 2026 was
`michelescandola/scando-lab`, commit
`cc6841abc344eba04f981837a056baf20de10a62`.

Portraits retain transparency and were resized for web use. The two student
profiles with no source URL omit the profile link until a URL is supplied.
