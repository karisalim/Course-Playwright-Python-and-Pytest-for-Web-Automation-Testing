from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    # launch a browser
    browser = p.chromium.launch(headless=False,
        slow_mo=500)
    
    # create open a new page
    page = browser.new_page()
    # visit a website
    page.goto("https://playwright.dev/python/")
    # take a screenshot
    page.screenshot(path="playwright.png")

    # Locate a Link Element
    docs_btn= page.get_by_role("link", name="Docs").click()

    # Get the url
    print("Docs URL: ", page.url)
    # close the browser
    browser.close()