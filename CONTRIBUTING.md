# Contributing to Scando-lab

Most content changes require Markdown or YAML only. You do not need to edit
HTML, CSS or JavaScript to add a person, publication, research theme,
activity or resource.

## Choose the file

| Change | Edit |
| --- | --- |
| Home introduction | `includes/home-hero.qmd` or `includes/home-perspective.qmd` |
| Research themes | `content/research.yml` |
| Open science text | `open-science.qmd` |
| Team profiles | `content/people.yml` |
| Activities introduction | `activities.qmd` |
| An announcement, talk or workshop | `content/activities.yml` |
| Publications | `content/publications.yml` |
| Resource links | `content/resources.yml` |
| Contact details | `contact.qmd` |
| Page titles and introductions | YAML front matter at the top of the corresponding `.qmd` |
| Navigation labels and order | `site-navigation` in `_quarto.yml` |

## Edit in GitHub

1. Open the relevant file and choose the pencil icon.
2. Edit an existing entry, or copy a complete entry and change its fields.
3. Give the change a short description and propose it on a new branch.
4. Open a pull request. The **Build and deploy Quarto** workflow renders the
   whole website and checks local links and page structure.
5. Have another contributor review the content before merging.

Pull requests run checks without deploying. After a reviewed change is merged
into `main`, the same workflow checks the complete website and publishes it
to GitHub Pages. The result appears under **Actions** and the `github-pages`
deployment environment.

## Preview locally

Install [Quarto](https://quarto.org/docs/get-started/) and run these commands
from the project directory:

```sh
quarto preview
```

To render every page and check local links:

```sh
quarto render
python3 scripts/check_site.py
```

Quarto alone is enough to render the site. Python is used only for the optional
link checker and is already available on the GitHub Actions runner.

## YAML conventions

Keep the indentation at two spaces and preserve the dash at the start of each
entry. The numeric `order` field controls display order in lists other than
publications; publications sort automatically by their `published` field. Use `>-` for a long
paragraph. Descriptions in the content lists are plain text; page bodies use
Markdown. Quote a short value when it contains a colon.

### Add a publication

Append an entry to `content/publications.yml`:

```yaml
- title: "Replace with the publication title"
  authors: "A. Author, M. Scandola"
  venue: "Journal or preprint server"
  published: "2026-07-13"
  publication_type: "Journal article"
  topics: [methods, neuropsychology]
  url: "https://example.org/replace-with-the-real-publication-link"
  source_url: "https://example.org/replace-with-the-bibliographic-record"
  date_source_url: "https://example.org/replace-with-the-publication-date-source"
```

Use one or more of these topic IDs. A work appears once in the complete list
and is available through every assigned topic:

| Topic ID | Displayed topic |
| --- | --- |
| `methods` | Open Science, Statistics, and Methods |
| `pain-body` | Pain and body representation |
| `action` | Action representation |
| `space` | Space representation |
| `society` | Society |
| `neuropsychology` | Neuropsychology |

The topic labels and filter order are defined in `publications.qmd` under
`listing.template-params.topics`. No JavaScript edits are needed to assign topics.

Use a quoted ISO date for `published`: `"2026-07-13"`, `"2026-07"`, or `"2026"`.
Prefer the first online publication date, not a later print issue or the date
the record was deposited in a repository. Keep only the precision the source
actually supports. Within the same year, year-only records follow dated works;
within a month, month-only records follow works with a known day. Exact date
ties are ordered alphabetically by title. New entries need no `order` number
and can be appended anywhere in the YAML file.

Keep the publication type explicit: for example, `Journal article`, `Preprint`,
`Conference poster`, `Conference abstract`, `Conference contribution`, `Book chapter`,
`Software` or `Correction`. Supply the title, authors and venue separately.
For unusually large author lists, give the first authors and `et al.`, indicate
M. Scandola's participation when needed, and link to the complete author record.
Optional `doi` and `note` fields can record an identifier or a short factual note.
Replace all example URLs before submitting. The public page links `url` and
`source_url`; `date_source_url` preserves the evidence for future maintenance.

The 12 November 2026 update contains 102 records from the University of Verona
[IRIS author profile](https://iris.univr.it/cris/rp/rp08237?type=all), two methods
preprints retained from the original page, and three additional distinct DOI
works verified in [ORCID](https://orcid.org/0000-0003-0853-8975). Publisher,
Crossref and PubMed metadata refine dates where available. IRIS's generic
1 January dates are treated as year-only unless a publication date was
independently verified. Google Scholar blocked access during this update,
so this is not claimed to be a complete export of that profile. Older ORCID
conference records without verified author lists have not been added.
Preprint versions of listed journal articles are not added as separate works;
conference presentations and corrections remain explicitly labelled records.
Topic assignments are editorial and can be revised by the lab.

### Add a person

Append an entry to `content/people.yml`:

```yaml
- order: 6
  title: "Full name"
  role: "Role · Affiliation"
  description: >-
    A short description of the person's research interests.
  image: "imgs/portrait.png"
  initials: "AB"
  profile_url: ""
```

Put the image in `imgs/`. If a portrait is unavailable, set `image: ""` and
provide initials. Leave `profile_url: ""` when no verified URL is available;
the site will omit the link. Please keep portraits small and square; the
current images are 225 × 225 px and display at 75 × 75 px.

### Add an activity

The initial activity list is intentionally empty. Replace its `[]` with a
list such as this, using a real event and verified details:

```yaml
- order: 1
  title: "Replace with the activity title"
  date_label: "Replace with the actual date or date range"
  description: >-
    Include a short summary and the location or participation details.
  url: ""
```

Later activities are additional entries in the same list. The empty-state
message disappears automatically when an activity is added. Use a blank URL
if the announcement has no separate registration or details page.

### Add a resource

Append an entry to `content/resources.yml`:

```yaml
- order: 5
  title: "Resource title"
  kind: "Code, data, teaching material, preprint or network"
  description: >-
    Briefly explain what the resource provides.
  url: "https://example.org/replace-with-the-real-resource-link"
```

### Edit research themes

Edit `content/research.yml`. The `card_class` value controls card width:
`large highlight`, `medium` or `third`. Use `third` for another standard card.
The displayed number is generated from `order`.

## Add another top-level page

Copy a page such as `contact.qmd`, then update its `title`, `pagetitle`,
`description`, `page-id`, `page-heading` and `page-lead`. Add the source to
`project.render` and a menu entry to `site-navigation` in `_quarto.yml`.
The navigation entry's `id` must match the page's `page-id`.

## Layout changes

Shared HTML and listing templates are in `templates/`. The original design
is in `assets/css/styles.css`; multipage additions are in
`assets/css/multipage.css`. `assets/js/site.js` provides mobile navigation,
current-page highlighting and publication filters.

Build output in `_site/` and Quarto's `.quarto/` cache are ignored by Git.
Edit the sources, then render again.
