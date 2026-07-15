# LocalGov Django

A complete Django port of [LocalGov Drupal](https://localgovdrupal.org/) — the open source publishing platform built collaboratively by UK councils.

LocalGov Django replicates the LocalGov Drupal feature set using Django best practices, with the exact same [LocalGov Base](https://github.com/localgovdrupal/localgov_base) theme styling.

**Documentation:** https://kurtisrogers.github.io/LocalGov-Django/

## Features

| LocalGov Drupal module | Django app | Content types |
|---|---|---|
| Services | `services` | Service landing, sub-landing, page, status |
| Directories | `directories` | Channel, page, organisation, venue |
| Guides | `guides` | Guide overview, guide page |
| Step by step | `step_by_step` | Overview, step page |
| News | `news` | Newsroom, news article |
| Events | `events` | Event |
| Subsites | `subsites` | Subsite overview, subsite page |
| Alert banners | `alerts` | Alert banner |
| Sitewide search | `search` | Cross-content search |
| Core | `core` | Topics, menus, site configuration |

## Quick start

```bash
git clone https://github.com/kurtisrogers/LocalGov-Django.git
cd LocalGov-Django
pip install -r requirements.txt
python manage.py migrate
python manage.py load_sample_content
python manage.py createsuperuser  # optional
python manage.py runserver
```

Visit http://localhost:8000 for the demo site.

## Admin

Content is managed via Django admin at `/admin/`.

## Testing

```bash
# Unit tests
pytest tests/ -k "not bdd"

# Playwright BDD tests (requires: playwright install chromium)
pytest tests/bdd/
```

## Project structure

```
config/          # Django settings and URL routing
core/            # Shared models, site config, menus, topics
services/        # Service content types
directories/     # Directory channels and entries
guides/          # Multi-page guides
step_by_step/    # Sequential step-by-step processes
news/            # Newsrooms and articles
events/          # Council events
subsites/        # Subsite microsites
alerts/          # Site-wide alert banners
search/          # Sitewide search
pages/           # Homepage
static/          # LocalGov Base theme CSS/JS/assets
templates/       # Django templates using LocalGov markup
tests/           # Unit and Playwright BDD tests
docs/            # MkDocs documentation (deployed to GitHub Pages)
```

## Styling

CSS is copied directly from the [localgov_base](https://github.com/localgovdrupal/localgov_base) theme (2.x branch), including CSS custom properties, grid layout, and all component styles.

## Documentation

Full documentation is built with MkDocs and deployed to GitHub Pages.

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

Visit http://127.0.0.1:8000 to preview docs locally.

## License

MIT — LocalGov Drupal is open source; this project is an independent Django implementation for developers who prefer the Django ecosystem.

## Credits

- [LocalGov Drupal](https://localgovdrupal.org/) — original distribution
- [LocalGov Base theme](https://github.com/localgovdrupal/localgov_base) — styling
