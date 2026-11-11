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
4. Open a pull request. The **Render and check Quarto** workflow renders the
   whole website and checks local links and page structure.
5. Have another contributor review the content before merging.

The workflow checks the source; it does not deploy a public website.

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
entry. The numeric `order` field controls display order. Use `>-` for a long
paragraph. Descriptions in the content lists are plain text; page bodies use
Markdown. Quote a short value when it contains a colon.

### Add a publication

Append an entry to `content/publications.yml`:

```yaml
- order: 9
  title: "Replace with the publication title"
  authors: "Author names · Journal or preprint server"
  year: 2026
  label: Methods
  category: statistics
  url: "https://example.org/replace-with-the-real-publication-link"
```

Choose `statistics` or `body` for `category`. These values match the filters.
If you introduce another category, also add its filter button in
`templates/publications.ejs.md`. Replace the example URL before submitting.

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
