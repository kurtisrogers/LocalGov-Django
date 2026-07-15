# For developers

LocalGov Django is a Django project that replicates the [LocalGov Drupal](https://localgovdrupal.org/) distribution. It delivers the default functionality most local councils need for web publishing, using Django best practices.

You will need some development resource to install, configure for an individual council's needs, and launch. It will also need appropriate hosting and security updates going forward.

Councils and suppliers can extend the default functionality with custom Django apps. We encourage contributions back to the project so other councils can benefit.

## Quick links

- Get set up locally: [Getting started](getting-started.md)
- Look at the code: [GitHub](https://github.com/kurtisrogers/LocalGov-Django)
- Read about the [Features](features/index.md)
- Frontend developers: [Theme](theme.md)
- Run the tests: [Testing](testing.md)
- See the [Roadmap](../roadmap.md)

## Project layout

```
config/          Django settings and URL routing
core/            Site config, menus, topics
services/        Service content types
directories/     Directory channels and entries
guides/          Guide overviews and pages
step_by_step/    Step-by-step processes
news/            Newsrooms and articles
events/          Council events
subsites/        Subsite overviews and pages
alerts/          Alert banners
search/          Sitewide search
pages/           Homepage
static/          LocalGov Base theme assets
templates/       Django templates
tests/           Unit and Playwright BDD tests
```

See [Project structure](project-structure.md) for more detail.

## Get involved

LocalGov Django needs developers to help push forward features and issues. If you are a developer in a council or supplier, please [open an issue](https://github.com/kurtisrogers/LocalGov-Django/issues) or submit a pull request.

For the wider LocalGov Drupal community (Slack, technical drop-ins, governance), see the [LocalGov Drupal developer docs](https://docs.localgovdrupal.org/devs/).
