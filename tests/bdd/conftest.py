"""Playwright BDD test configuration."""

import pytest
from django.core.management import call_command
from playwright.sync_api import expect, sync_playwright

# live_server uses transactional_db; do not use django_db(transaction=True).


@pytest.fixture(scope="session")
def django_db_modify_db_settings():
    """Increase SQLite lock timeout for live_server + Playwright on CI."""
    return {
        "default": {
            "OPTIONS": {
                "timeout": 30,
            },
        },
    }


@pytest.fixture(autouse=True)
def load_sample_content(transactional_db):
    """Load demo content once per test before scenarios run."""
    call_command("load_sample_content")


@pytest.fixture
def browser_page(live_server):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        page._live_server = live_server
        yield page
        browser.close()


def assert_visible(page, locator):
    """Assert locator is visible with CI-friendly timeout."""
    expect(locator.first).to_be_visible(timeout=10_000)
