# Features

Technical documentation for LocalGov Django features, mirroring the [LocalGov Drupal features](https://docs.localgovdrupal.org/devs/features/) documentation.

## Services

Django app: `services`

Content types:

| Model | Description |
| --- | --- |
| `ServiceLandingPage` | Top-level section for each service |
| `ServiceSubLandingPage` | Index page within a service |
| `ServicePage` | Basic page in a service hierarchy |
| `ServiceStatus` | Status update with severity (minor, major, announcement, notable person) |

URLs: `/services/`, `/services/<slug>/`, `/services/<service_slug>/page/<slug>/`

## Alert banners

Django app: `alerts`

Model: `AlertBanner` with types `announce`, `minor`, `major`, `notable-person`.

Active banners are injected via the `site_context` template processor and rendered in `templates/includes/alert_banners.html`.

## News

Django app: `news`

| Model | Description |
| --- | --- |
| `Newsroom` | Listing page for articles |
| `NewsArticle` | Article with date, featured flag, categories |

URLs: `/news/`, `/news/<slug>/`, `/news/<newsroom_slug>/<year>/<slug>/`

## Directories

Django app: `directories`

| Model | Description |
| --- | --- |
| `DirectoryChannel` | Searchable/filterable listing page |
| `DirectoryFacet` / `DirectoryFacetType` | Facet filtering |
| `DirectoryPage` | General-purpose entry |
| `DirectoryOrganisation` | Organisation with contact details |
| `DirectoryVenue` | Venue with location |

Channel detail view supports `?q=` search and `?facet=` filtering.

## Guides

Django app: `guides`

`GuideOverview` with child `GuidePage` models. Pages include `previous_page` and `next_page` properties for navigation.

## Step by step

Django app: `step_by_step`

`StepByStepOverview` with numbered `StepByStepPage` steps and prev/next navigation.

## Events

Django app: `events`

`Event` model with start/end dates, location, and optional coordinates.

## Subsites

Django app: `subsites`

`SubsiteOverview` with child `SubsitePage` models.

## Sitewide search

Django app: `search`

`SitewideSearchView` searches across all published content types. Uses database `icontains` queries; Solr integration is on the [roadmap](../../roadmap.md).

## Core

Django app: `core`

| Model | Description |
| --- | --- |
| `SiteConfiguration` | Council name, contact details, branding |
| `MenuItem` | Primary, secondary, and footer navigation |
| `Topic` | Taxonomy for categorising content |
| `PublishableModel` | Abstract base with title, slug, body, published flag |
