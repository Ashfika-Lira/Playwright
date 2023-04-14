from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"login-button\"]").click()
    error_text = page.locator("//h3[@data-test='error']").inner_text()
    print(error_text)
    page.locator('#user-name').fill("standard_user")
    entered_value = page.locator('#user-name').input_value()
    print(entered_value)
    login_btn = page.locator("#login-button")
    print(login_btn.input_value())
