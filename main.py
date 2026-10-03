from browser.browser_manager import login_and_save_session


def main():
    print("WebBinder started.")

    login_url = "https://bcourses.berkeley.edu/"
    login_and_save_session(login_url)


if __name__ == "__main__":
    main()