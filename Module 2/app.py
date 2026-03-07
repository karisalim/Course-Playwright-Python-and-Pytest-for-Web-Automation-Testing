from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    # launch a browser
    browser = p.chromium.launch(headless=False,
        slow_mo=8000)
    
    # create open a new page
    page = browser.new_page()
    # visit a website
    page.goto("https://bootswatch.com/default/")
   
    # Locate a Link Element
    btn= page.get_by_role("button", name="Default button")

    # radio button
    radio_btn= page.get_by_role("radio", name="Option one is this and that—be sure to include why it's great")

    # Highlight the element
    radio_btn.highlight()

    # Chech box
    check_box= page.get_by_role("checkbox", name="Default checkbox")

    #highlight the check_box
    check_box.highlight()

    # Click the element
    # btn.click()

    # close the browser
    browser.close()