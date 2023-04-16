from playwright.sync_api import Page, expect


def test_file_upload(page: Page) -> None:
    page.goto("https://www.google.com/")

    search_input = page.get_by_role("combobox", name="সার্চ করুন")
    search_input.click()
    # search_input.fill("Playwright")

    page.keyboard.press('P')
    page.keyboard.press('l')
    page.keyboard.press('a')
    page.keyboard.press('y')

    page.wait_for_timeout(3000)

    search_input.blur()

    page.keyboard.press('W')
    page.keyboard.press('R')
    page.keyboard.press('G')
    page.keyboard.press('H')

    page.wait_for_timeout(3000)

    value = search_input.input_value()

    print(value)

    expect(search_input).to_have_value('Play')
