
from playwright.sync_api import Page


def test_page_source(page: Page) -> None:
    page.goto("https://www.google.com/")
    print(page.content())

