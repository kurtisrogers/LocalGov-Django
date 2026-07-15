# For content designers and editors

LocalGov Django provides the same content types as [LocalGov Drupal](https://docs.localgovdrupal.org/content/) for council web publishing.

Content is managed through Django admin at `/admin/`. This documentation describes the content types and how they map to citizen-facing pages.

## Quick links

- [Content types](features/content-types.md)
- [Services](features/services.md)
- [Directories](features/directories.md)
- [News](features/news.md)
- [Alert banners](features/alert-banners.md)
- [Features overview](features/index.md)

## Content patterns

LocalGov Drupal content follows these patterns, which LocalGov Django replicates:

### Services

Council services are organised in a two-level hierarchy:

1. **Service landing page** — top-level service (e.g. "Bins and recycling")
2. **Service sub-landing page** — section within a service (e.g. "Bin collections")
3. **Service page** — individual information or task page

Service status updates can be shown on service landing pages.

### Guides and step by step

- **Guides** — related pages the user can browse in any order
- **Step by step** — sequential process the user follows step by step

### Directories

Directories present searchable lists of organisations, venues, or pages. Facets allow filtering (e.g. school age, location).

### News and events

- **Newsrooms** list articles with optional featured items
- **Events** appear in chronological listings

## Admin tips

- Use clear, descriptive titles — slugs are auto-generated
- Write a summary for listing pages and search results
- Tag content with **Topics** for categorisation
- Unpublish rather than delete content you may need again
