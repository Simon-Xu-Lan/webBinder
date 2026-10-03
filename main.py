from browser.browser_manager import open_login_page


def main():
    print("WebBinder started.")

    login_url = "https://study.dataapplab.com/course?courseid=llm-developer-bootcamp-2603"
    open_login_page(login_url)


if __name__ == "__main__":
    main()