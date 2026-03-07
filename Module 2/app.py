from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    # launch a browser
    browser = p.chromium.launch(headless=False,
        slow_mo=500)
    
    # create open a new page
    page = browser.new_page()
    # visit a website
    page.goto("https://playwright.dev/python/")
   
    # Locate a Link Element
    get_started_btn= page.get_by_role("link", name="Get started")

    # Highlight the element
    get_started_btn.highlight()

    # Click the element
    get_started_btn.click()


    # close the browser
    browser.close()