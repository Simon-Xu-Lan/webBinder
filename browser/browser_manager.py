from playwright.sync_api import sync_playwright
from browser.session_manager import save_session


def login_and_save_session(url: str):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=False                      # headless=False 显示 browser window, True: browser 会在后台运行，看不到窗口。
        )

        # page = browser.new_page()               # 创建一个新的 browser tab/page。
        # page.goto(url)                          # 访问指定网页。
        
        # use context
        context = browser.new_context()

        page = context.new_page()

        page.goto(url)

        print("Login page opened.")
        print("Please complete login manually in the browser.")

        input("After login is completed, press Enter here...")

        print()
        print("Login confirmation received.")
        print(f"Current page title: {page.title()}")
        print(f"Current URL: {page.url}")

        save_session(context)

        input("Session saved. Press Enter to close the browser...")

        browser.close()