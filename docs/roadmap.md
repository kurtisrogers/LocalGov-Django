# Product roadmap

The [LocalGov Drupal product roadmap](https://localgovdrupal.org/products/product-roadmap) is set by councils, suppliers, and the core team. LocalGov Django tracks these missions and ports features as they stabilise in the Drupal distribution.

## LocalGov Drupal 2026 missions

The LocalGov Drupal community has arranged its work into missions based on feedback from council users and suppliers:

1. **Drupal 11 upgrade**
2. **Refresh service landing pages**
3. **Local Government Reorganisation** (if needed by existing or new councils)
4. **Search with Solr and AI**
5. **AI tools for content designers**
6. **Microsites**

LocalGov Drupal is also exploring intranet use cases.

## What LocalGov Drupal is working on now

| Update | By |
| --- | --- |
| Drupal 11 upgrade | Core team and community |
| Accessibility audit of LGD CMS and LGD Microsites, with follow-on remediation | Core team |

Find more details on the [LocalGov Drupal backlog](https://github.com/orgs/localgovdrupal/projects).

## Community Fund

The LocalGov Drupal Community Fund enables councils and suppliers to co-fund bigger projects not covered by the core roadmap. Once complete, work is open-sourced for everyone.

Examples of Community Fund projects include elections v4, PDF importer, insight dashboard, quality metrics, and specialist planning publishing.

## LocalGov Django port status

This table maps LocalGov Drupal roadmap areas to the Django port. Status reflects the current `main` branch.

| LocalGov Drupal area | LocalGov Django status | Notes |
| --- | --- | --- |
| Service landing pages | <span class="lgd-status-done"></span> Implemented | Landing, sub-landing, page, status |
| Service landing page refresh | <span class="lgd-status-partial"></span> Partial | Base theme styling in place; refresh TBD |
| Directories | <span class="lgd-status-done"></span> Implemented | Channels, facets, search |
| Guides | <span class="lgd-status-done"></span> Implemented | Overview + pages with navigation |
| Step by step | <span class="lgd-status-done"></span> Implemented | Overview + numbered steps |
| News | <span class="lgd-status-done"></span> Implemented | Newsroom + articles |
| Events | <span class="lgd-status-done"></span> Implemented | Listings and detail pages |
| Alert banners | <span class="lgd-status-done"></span> Implemented | Four severity types |
| Subsites | <span class="lgd-status-partial"></span> Partial | Overview + pages; full microsite platform planned |
| Microsites | <span class="lgd-status-planned"></span> Planned | Separate multi-site architecture |
| Sitewide search | <span class="lgd-status-partial"></span> Partial | Database search; Solr integration planned |
| Search with Solr and AI | <span class="lgd-status-planned"></span> Planned | Follow LocalGov Drupal Solr work |
| AI tools for content designers | <span class="lgd-status-planned"></span> Planned | — |
| Workflows | <span class="lgd-status-planned"></span> Planned | Editorial workflow and moderation |
| Elections | <span class="lgd-status-planned"></span> Planned | — |
| Publications | <span class="lgd-status-planned"></span> Planned | — |
| Paragraphs / page builder | <span class="lgd-status-planned"></span> Planned | Callout boxes, tabs, media blocks |
| Accessibility audit remediation | <span class="lgd-status-partial"></span> In progress | LocalGov Base skip links, ARIA, focus styles |
| Intranet exploration | <span class="lgd-status-planned"></span> Planned | — |

## How we design and build

LocalGov Drupal uses the UK Design Council's [Double Diamond](https://www.designcouncil.org.uk/our-resources/framework-for-innovation/) framework. LocalGov Django follows the same content patterns and LocalGov Base design system so councils get a consistent citizen experience regardless of backend.

## Contributing to the roadmap

LocalGov Django is community-driven. To propose a feature:

1. Check the [LocalGov Drupal roadmap](https://localgovdrupal.org/products/product-roadmap) and backlog
2. [Open an issue](https://github.com/kurtisrogers/LocalGov-Django/issues) describing the Django port requirement
3. Submit a pull request following [contributing guidelines](contributing/index.md)

Priority is given to features that exist in LocalGov Drupal and benefit multiple councils.
