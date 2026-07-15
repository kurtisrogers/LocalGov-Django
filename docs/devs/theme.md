# Theme

LocalGov Django uses the [LocalGov Base](https://github.com/localgovdrupal/localgov_base) theme (2.x branch) for styling. CSS, JavaScript, and favicon assets are copied to `static/localgov_base/`.

## CSS

Styles are loaded in `templates/includes/localgov_css.html` in the same order as `localgov_base.libraries.yml`:

- Base: variables, base, layout utilities, fields
- Components: header, footer, breadcrumbs, box-links, service pages, directories, news, events, and more

CSS custom properties (variables) are defined in `static/localgov_base/css/base/variables.css`. Override these in a council sub-theme by creating a custom CSS file.

## Templates

Django templates mirror LocalGov Drupal Twig markup:

| Template | Purpose |
| --- | --- |
| `templates/base.html` | HTML shell, CSS/JS includes |
| `templates/includes/header.html` | `lgd-header` with menu toggles |
| `templates/includes/footer.html` | `lgd-footer` regions |
| `templates/includes/breadcrumbs.html` | Breadcrumb navigation |
| `templates/includes/alert_banners.html` | Alert banner component |

## JavaScript

`static/localgov_base/js/header-vanilla.js` is a vanilla JS port of the Drupal `header.js` behaviour (mobile menu toggles, ESC key handling).

## Customisation

To customise for a council:

1. Override CSS variables in a new stylesheet
2. Extend `templates/base.html` and override blocks
3. Replace `SiteConfiguration` values in admin or via fixtures

## Regions

The header provides these regions matching LocalGov Base:

- Header (site name)
- Primary menu + search
- Secondary menu (services)
- Footer (three columns + copyright)
