# Contributing

Thank you for helping improve LocalGov Django.

## Ways to contribute

### Report issues

[Open an issue](https://github.com/kurtisrogers/LocalGov-Django/issues) for bugs, missing features, or documentation gaps.

### Submit pull requests

1. Fork the repository
2. Create a branch from `main`
3. Make focused changes with tests
4. Run `pytest tests/ -p no:playwright`
5. Open a pull request with a clear description

### Improve documentation

Documentation lives in the `docs/` folder and is built with MkDocs. To preview locally:

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to preview changes.

## Development guidelines

- Follow existing code conventions in each Django app
- Keep imports at the top of files
- Use exhaustive switch handling for TypeScript unions (where applicable)
- Add unit tests for new behaviour
- Add BDD scenarios for user-facing flows where appropriate

## Alignment with LocalGov Drupal

When adding features, reference the equivalent [LocalGov Drupal documentation](https://docs.localgovdrupal.org/) and check the [roadmap](../roadmap.md) for priority.

Features that exist in LocalGov Drupal should match its content model and URL patterns where practical.

## Code of conduct

Be respectful and constructive. LocalGov Django is part of the wider local government open source community alongside [LocalGov Drupal](https://localgovdrupal.org/).
