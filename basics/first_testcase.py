from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="সার্চ করুন").click()
    page.get_by_role("combobox", name="সার্চ করুন").fill("playwright")
    page.get_by_role("combobox", name="সার্চ করুন").press("Enter")
    page.get_by_role("link", name="Playwright: Fast and reliable end-to-end testing for modern ... playwright.dev https://playwright.dev").click()

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace.zip")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

