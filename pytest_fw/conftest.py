import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


@pytest.fixture()
def set_up_tear_down(page) -> None:
    # context = browser.new_context()
    # page = context.new_page()
    page.set_viewport_size({"width": 1536, "height": 800})
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user", timeout=5000)
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    yield page


@pytest.fixture()
def set_up_tear_down_no_login(page) -> None:
    page.set_viewport_size({"width": 1536, "height": 800})
    page.goto("/")
    yield page
