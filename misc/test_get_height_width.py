from playwright.sync_api import Page, expect


def test_get_height_width(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")

    login_btn = page.get_by_text("Login")

    box = login_btn.bounding_box()
    height = box['height']
    width = box['width']

    print(f"Height of login button is {height}")
    print(f"Width of login button is {width}")