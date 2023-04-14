from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/sortable")
    page.get_by_role("banner").click(button="right")
    page.get_by_role("link").click()
    page.goto("https://demoqa.com/sortable")
    page.get_by_role("tabpanel", name="List").get_by_text("One").click()
    page.get_by_role("tabpanel", name="List").get_by_text("Three").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
