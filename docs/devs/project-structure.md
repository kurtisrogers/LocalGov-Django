# Project structure

## Django apps

Each LocalGov Drupal module maps to a Django app:

| App | LocalGov Drupal equivalent |
| --- | --- |
| `core` | `localgov_core` |
| `services` | `localgov_services` |
| `directories` | `localgov_directories` |
| `guides` | `localgov_guides` |
| `step_by_step` | `localgov_step_by_step` |
| `news` | `localgov_news` |
| `events` | `localgov_events` |
| `subsites` | `localgov_subsites` |
| `alerts` | `localgov_alert_banner` |
| `search` | `localgov_search` |
| `pages` | Front page |

## Models

All content models inherit from `core.models.PublishableModel` which provides:

- `title`, `slug`, `summary`, `body`
- `published` boolean flag
- `created` / `modified` timestamps (via django-model-utils)

## Views

Class-based views (`ListView`, `DetailView`) with URL namespacing. Unpublished content returns 404 via `core.views.get_published_or_404`.

## Admin

Each app registers models in `admin.py` with:

- `prepopulated_fields` for slugs
- `list_display` and `list_filter`
- Inline editing for parent/child relationships

## Static files

WhiteNoise serves compressed static files. In development, files are read from `static/`. Run `collectstatic` for production.

## Templates

Global templates in `templates/` with app-specific subdirectories (`services/`, `directories/`, etc.).

Context processors in `core/context_processors.py` inject site config, menus, and active alerts.
