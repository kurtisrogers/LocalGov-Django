# Testing

LocalGov Django includes unit tests and Playwright BDD scenarios.

## Unit tests

```bash
pytest tests/ -k "not bdd" -p no:playwright
```

Tests cover:

- Site configuration singleton
- Homepage and service views
- Directory search and facet filtering
- Guide and step-by-step navigation
- Sitewide search

## Playwright BDD tests

BDD scenarios use pytest-bdd with Gherkin feature files in `tests/bdd/features/`:

```bash
pip install -r requirements.txt
playwright install chromium
pytest tests/bdd/ -p no:playwright
```

Scenarios cover homepage branding, services browsing, and sitewide search.

!!! note
    BDD tests use pytest-django's `transactional_db` fixture so the live server thread can access database content.

## CI

GitHub Actions runs unit tests and BDD tests on every push and pull request. See `.github/workflows/ci.yml`.

## Writing new tests

- Unit tests: add to `tests/test_*.py` using `django.test.TestCase`
- BDD: add `.feature` files and step definitions in `tests/bdd/`
