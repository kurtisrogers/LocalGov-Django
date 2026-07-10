"""BDD step definitions for Playwright tests (sync API)."""

from urllib.parse import urljoin

import pytest
from django.core.management import call_command
from playwright.sync_api import sync_playwright
from pytest_bdd import given, parsers, scenarios, then, when

scenarios("features/homepage.feature")
scenarios("features/services.feature")
scenarios("features/search.feature")


@pytest.fixture
def browser_page(live_server):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        page._live_server = live_server
        yield page
        browser.close()


@given("the sample content is loaded")
def sample_content_loaded(db):
    call_command("load_sample_content")


@when("I visit the homepage")
def visit_homepage(browser_page):
    browser_page.goto(browser_page._live_server.url)


@when("I visit the services page")
def visit_services(browser_page):
    browser_page.goto(urljoin(browser_page._live_server.url, "/services/"))


@when(parsers.parse('I visit "{path}"'))
def visit_path(browser_page, path):
    browser_page.goto(urljoin(browser_page._live_server.url, path))


@when(parsers.parse('I search for "{query}"'))
def search_site(browser_page, query):
    browser_page.goto(urljoin(browser_page._live_server.url, f"/search/?q={query}"))


@then(parsers.parse('I should see "{text}"'))
def should_see_text(browser_page, text):
    browser_page.wait_for_load_state("domcontentloaded")
    locator = browser_page.get_by_role("heading", name=text)
    if locator.count() == 0:
        locator = browser_page.get_by_text(text)
    assert locator.first.is_visible()


@then(parsers.parse('I should see a link to "{text}"'))
def should_see_link(browser_page, text):
    assert browser_page.get_by_role("link", name=text).first.is_visible()
