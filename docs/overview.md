# Overview

A brief overview of LocalGov Django and its features.

LocalGov Django is the publishing platform that brings [LocalGov Drupal](https://localgovdrupal.org/) patterns to the Django ecosystem. It is built for councils, suppliers, and developers who want the same local government content model and styling without Drupal.

## Feature summary

| Feature | Django app | Status |
| --- | --- | --- |
| Services | `services` | Implemented |
| Directories | `directories` | Implemented |
| Guides | `guides` | Implemented |
| Step by step | `step_by_step` | Implemented |
| News | `news` | Implemented |
| Events | `events` | Implemented |
| Subsites | `subsites` | Implemented |
| Alert banners | `alerts` | Implemented |
| Sitewide search | `search` | Implemented |
| Workflows | — | Planned |
| Microsites | — | Planned |
| Elections | — | Planned |
| Publications | — | Planned |

See the [roadmap](roadmap.md) for alignment with LocalGov Drupal missions.

## Services

Provides pages and navigation for presenting the services provided by local government.

Content types:

- **Service landing page** — the top level section for each service
- **Service sub-landing page** — detail and links to specific pages within a service
- **Service page** — the basic page placed in a service hierarchy
- **Service status** — optional updates about the status of a service

Other content types can be linked from service landing and sub-landing pages.

[Developer documentation →](devs/features/index.md#services) · [Content documentation →](content/features/services.md)

## Alert banners

Site-wide or service-specific alert banners with severity types:

- Announcement
- Minor
- Major
- Notable person

[Developer documentation →](devs/features/index.md#alert-banners) · [Content documentation →](content/features/alert-banners.md)

## News

- **Newsroom** — page for listing and featuring news articles
- **News article** — stand-alone article with date, categories, and featured flag

[Developer documentation →](devs/features/index.md#news) · [Content documentation →](content/features/news.md)

## Directories

Searchable directory channels with facet filtering. Entry types:

- Directory page (general purpose)
- Directory organisation (libraries, schools)
- Directory venue (parks, sports facilities)

[Developer documentation →](devs/features/index.md#directories) · [Content documentation →](content/features/directories.md)

## Guides and step by step

- **Guides** — connected pages with previous/next navigation
- **Step by step** — sequential numbered steps for processes

## Events

Council events with start/end dates, location, and optional map coordinates.

## Subsites

Subsite overviews with child pages for council microsites and themed sections.

## Sitewide search

Cross-content search across services, directories, guides, news, events, and more.

## Styling

LocalGov Django uses the [LocalGov Base](https://github.com/localgovdrupal/localgov_base) theme CSS copied into `static/localgov_base/`. Templates mirror the Drupal theme markup.

[Theme documentation →](devs/theme.md)
