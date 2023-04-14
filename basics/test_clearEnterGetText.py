import time
from textwrap import fill

from playwright.sync_api import Page, expect


def clear_input_text(page, loc):
    page.locator(loc).press("Control+KeyA")
    page.locator(loc).press("Backspace")


def test_example(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("username1", timeout=90000)
    # Clear input field
    # page.locator("#username").fill("")
    clear_input_text(page, '#username')
    page.locator("#username").fill("tomsmith")
    time.sleep(5)
