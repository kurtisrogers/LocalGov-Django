"""BDD step definitions for Playwright tests (sync API)."""

from urllib.parse import urljoin

from pytest_bdd import given, parsers, scenarios, then, when

from tests.bdd.conftest import assert_visible

scenarios("features/homepage.feature")
scenarios("features/services.feature")
scenarios("features/search.feature")


@given("the sample content is loaded")
def sample_content_loaded(load_sample_content):
    """Sample content is loaded by autouse fixture in conftest."""


@when("I visit the homepage")
def visit_homepage(browser_page):
    browser_page.goto(browser_page._live_server.url)
    browser_page.wait_for_load_state("networkidle")


@when("I visit the services page")
def visit_services(browser_page):
    browser_page.goto(urljoin(browser_page._live_server.url, "/services/"))
    browser_page.wait_for_load_state("networkidle")


@when(parsers.parse('I visit "{path}"'))
def visit_path(browser_page, path):
    browser_page.goto(urljoin(browser_page._live_server.url, path))
    browser_page.wait_for_load_state("networkidle")


@when(parsers.parse('I search for "{query}"'))
def search_site(browser_page, query):
    browser_page.goto(urljoin(browser_page._live_server.url, f"/search/?q={query}"))
    browser_page.wait_for_load_state("networkidle")


@then(parsers.parse('I should see "{text}"'))
def should_see_text(browser_page, text):
    heading = browser_page.get_by_role("heading", name=text)
    if heading.count() > 0:
        assert_visible(browser_page, heading)
        return
    assert_visible(browser_page, browser_page.get_by_text(text))


@then(parsers.parse('I should see a link to "{text}"'))
def should_see_link(browser_page, text):
    assert_visible(browser_page, browser_page.get_by_role("link", name=text))
