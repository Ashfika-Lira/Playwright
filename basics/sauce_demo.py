from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user", timeout=5000)

    page.locator("#password").fill("secret_sauce")


    page.locator("#login-button").click()

    products_header = page.locator("//span[text()='Products']")

    assert products_header.is_visible(), "Login failed"

    burger_menu = page.locator("#react-burger-menu-btn")

    page.pause()

    burger_menu.click()

    logout_btn = page.locator("//div[@class='bm-menu']//a[text()='Logout']")

    page.pause()

    logout_btn.click()

    login_btn = page.locator("#login-button")

    assert login_btn.is_visible(), "Login unsuccessful"

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
