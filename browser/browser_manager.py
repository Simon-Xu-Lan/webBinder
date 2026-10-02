from playwright.sync_api import sync_playwright


def open_browser(url: str):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto(url)

        print(f"Opened page: {page.title()}")

        input("Press Enter to close the browser...")

        browser.close()