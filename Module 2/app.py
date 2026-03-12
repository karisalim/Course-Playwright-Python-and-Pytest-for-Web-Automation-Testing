from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    # launch a browser
    browser = p.chromium.launch(headless=False,
        slow_mo=8000)
    
    # create open a new page
    page = browser.new_page()
    # visit a website
    page.goto("https://bootswatch.com/default/")
   
    # # Locate a Link Element
    # btn= page.get_by_role("button", name="Default button")

    # # radio button
    # radio_btn= page.get_by_role("radio", name="Option one is this and that—be sure to include why it's great")

    # # Highlight the element
    # radio_btn.highlight()

    # # Chech box
    # check_box= page.get_by_role("checkbox", name="Default checkbox")

    # #highlight the check_box
    # check_box.highlight()
    # check_box.check()

    print("--"*20) ## video Locators-input-field

    # email_input = page.get_by_label("Email address")
    # email_input.highlight()

    # password_input = page.get_by_label("Password")
    # password_input.highlight()

    # # get by placeholder
    # page.get_by_placeholder("Enter email").highlight()

    # print("--"*20) ## video locator-text

    # page.get_by_text("with faded secondary").highlight()

    # # exact false will match the text if it contains the text كدا يقدر يلاقي التكست حتى لو كان فيه حاجات تانية معاه
    # page.get_by_text("Cum sociis natoque", exact=False).highlight() 

    # # exact true will match the text if it is exactly the same as the text كدا يقدر يلاقي التكست بس لو كان هو بالظبط كدا مش لو فيه حاجات تانية معاه
    # page.get_by_text("parturient montes", exact=True).highlight()

    # print("--"*20) ## video locator-title

    # page.get_by_title("attribute")


    print("--"*20) ## video Locating with CSS Selectors


    # page.locator("css=h1").highlight()
    # page.locator("footer").highlight()
    
    # Using a CSS selector (tag + class) to locate the button element

    # page.locator("button.btn-outline-success").highlight()
    # page.locator("button.btn-outline-success").click()
    
    # Using a CSS selector (id) to locate the button element
    # page.locator("button#btnGroupDrop1").click()
    
    # # Using a CSS selector (tag + class + id) to locate the button element
    # page.locator("input[readonly]").highlight()
    
    # # Using a CSS selector (attribute) to locate the button element   
    # page.locator("input[value='correct value']").highlight()
    
    # page.pause()
    
    print("--"*20) ## video CSS Selectors Hierarchy (Parent >> Child) (bg-dark >> nav.bg-dark > nav.bg-dark a.nav-link > nav.bg-dark a.nav-link.active )
    
    page.locator("nav.bg-dark a.nav-link.active").highlight() # parent
    
    page.pause()
    
    # Direct Child Selector (>) will select only the direct child elements of the parent element. It will not select the child elements of the child elements.
    
    page.locator("div.bs-component > ul.list-group").highlight()
    


    
    
    


    # close the browser
    browser.close()