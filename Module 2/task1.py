from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    # launch a browser
    browser = p.chromium.launch(headless=False,
        slow_mo=500)
    
    # create open a new page
    page = browser.new_page()
    # visit a website
    page.goto("https://the-internet.herokuapp.com/login")

    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")

    page.get_by_role("button", name="Login").click()

    page.get_by_role("link", name="Logout")

    
    browser.close()