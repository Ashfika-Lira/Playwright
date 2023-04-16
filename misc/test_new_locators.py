from playwright.sync_api import Page, expect


def test_new_locator_api(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    username = page.get_by_placeholder("Username")
    password = page.get_by_placeholder("Password")
    login_btn = page.get_by_text("Login")

    username.fill("standard_user")
    password.fill("secret_sauce")
    login_btn.click()


def test_new_locator_api2(page: Page) -> None:
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="সার্চ করুন").click()
    page.get_by_role("combobox", name="সার্চ করুন").press("CapsLock")
    page.get_by_role("combobox", name="সার্চ করুন").fill("P")
    page.get_by_role("combobox", name="সার্চ করুন").press("CapsLock")
    page.get_by_role("combobox", name="সার্চ করুন").fill("Playwright")
    page.get_by_text("playwright", exact=True).click()
    page.get_by_role("link",name="Playwright: Fast and reliable end-to-end testing for modern ... playwright.dev https://playwright.dev").click()


def test_new_locator_api3(page: Page) -> None:
    page.goto("https://demo.opencart.com/index.php?route=product/product&language=en-gb&product_id=40")

    quantity = page.get_by_label("Qty")

    expect(quantity).to_be_visible()
