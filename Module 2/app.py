from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    # launch a browser
    browser = p.chromium.launch(headless=False,
        slow_mo=500)
    
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
    
    # print("--"*20) ## video CSS Selectors Hierarchy (Parent >> Child) (bg-dark >> nav.bg-dark > nav.bg-dark a.nav-link > nav.bg-dark a.nav-link.active )
    
    # page.locator("nav.bg-dark a.nav-link.active").highlight() # parent
    
    # page.pause()
    
    # # Direct Child Selector (>) will select only the direct child elements of the parent element. It will not select the child elements of the child elements.
    
    # page.locator("div.bs-component > ul.list-group").highlight()

    
    print("--"*20) ## video CSS Selectors Pseudo Classes
    '''
    Pesudo Class is same funcation additional selector but it is used to select the elements based on their state or position in the DOM. It is used with the colon (:) symbol.
    # 📌 القاعدة
    
    tag : pseudo_class ( 'argument' )
    ↑  ↑      ↑              ↑
    h1  :    text         'Navbars'

    '''

    # page.locator("h1:text('Navbars')").highlight()

    # # هيختار كل H1 فيها كلمة nav في أي حتة
    # page.locator("h1:text('nav')")
    
    # #  هيختار H1 نصها بالظبط "Navs" بس    ( :text-is() — اختيار بالنص (Strict))
    # page.locator("h1:text-is('Navs')").highlight()

    # # 3️⃣ :visible — اختيار العناصر الظاهرة بس   (لو عندك عنصر بيظهر ويتخفى (زي Dropdown)، تقدر تختار اللي شايفه بس على الشاشة. )
    # page.locator("div.dropdown-menu:visible").highlight()

    # # 4️⃣ :nth-match() — اختيار عنصر بالرقم (Position)  (لو عندك 77 button بنفس الـ class، تقدر تختار الرابع بالظبط.)
    # #  الصيغة: :nth-match(selector, number)
    # page.locator("button.btn-primary").highlight() # >> 77 button

    # page.locator(":nth-match(button.btn-primary, 5)").highlight() # >> 5th button

    # page.locator(":nth-match(button:text('Primary'), 1)").highlight()
    

    '''
    ==============================================
    Pseudo Classes في Playwright - ملخص الدرس
    ==============================================

    1️⃣  :text('...') — بحث بالنص (Loose)
        بيختار أي عنصر يحتوي على النص، مش لازم بالظبط
        مثال: page.locator("h1:text('nav')")
        ✅ هيختار: "navbar" / "navigation" / "navbars"

    ---------------------------------------------

    2️⃣  :text-is('...') — بحث بالنص (Strict)
        بيختار العنصر اللي نصه بالظبط زي اللي كتبته
        مثال: page.locator("h1:text-is('Navbars')")
        ❌ مش هيختار: "nav" / "navbar"
        ✅ هيختار: "Navbars" بس

    ---------------------------------------------

    3️⃣  :visible — اختيار العناصر الظاهرة بس
        لو عندك عناصر بتظهر وتتخفى (Dropdowns / Modals)
        بيختار اللي ظاهر على الشاشة بس
        مثال: page.locator("div.dropdown-menu:visible")

    ---------------------------------------------

    4️⃣  :nth-match(selector, n) — اختيار بالرقم
        بيختار العنصر رقم n من مجموعة عناصر متشابهة
        ⚠️  لازم تبدأ بـ : من غير selector قبلها
        ⚠️  بتاخد argumentين: السيليكتور والرقم

        ❌ غلط: page.locator("button.btn-primary:nth-match(1)")
        ✅ صح:  page.locator(":nth-match(button.btn-primary, 1)")

        وتقدر تركب pseudo classes جوا بعض:
        مثال: page.locator(":nth-match(button:text('primary'), 3)")

    ==============================================
    ⚡ القاعدة العامة للـ Pseudo Class
    ==============================================

        tag:pseudo_class('argument')
        ↑  ↑     ↑           ↑
        h1  :    text        'nav'

    الـ colon : هو اللي بيفصل التاج عن الـ pseudo class

    ==============================================
    '''

    print("--"*20) ## video Locators XPath (XML Path Language) >>  لغة استعلام اتعملت أصلاً عشان تختار عناصر في XML، وبتشتغل على HTML كمان. أقوى من CSS في بعض الحالات بس شوية أصعب في الكتابة.

    '''
    1️⃣ الـ Absolute Path (المسار الكامل)
    بتبدأ من أول الصفحة وتنزل خطوة خطوة.
    /html/head/title

    page.locator("/html/head/title").highlight()
    #     ↑        ↑     ↑      ↑
    #  slash    html   head   title
    # (يعني ابدأ من الأول)

    2️⃣ الـ Relative Path (المسار النسبي)
    بتبدأ بـ // يعني "دور في أي حتة في الصفحة"

    / يعني "ابدأ من الأول"
    // يعني "دور في أي حتة في الصفحة"
    '''
 
    # ✅ هيلاقي كل H1 في الصفحة كلها (12 عنصر) 
    page.locator("xpath=//h1").highlight() 

    '''
    3️⃣ الاختيار بالـ Attribute
    بتحط الـ attribute جوا [] وقبل اسمه @
    //tag[@attribute='value']
    '''
    page.locator("//h1[@id='navbars']").highlight() # or write this >> page.locator("xpath=//h1[@id='navbars']").highlight()
    #               ↑   ↑       ↑
    #              tag  @id   'القيمة'

    page.locator("//input[@readonly]").highlight() # or write this >> page.locator("xpath=//input[@readonly]").highlight()
    
    '''
    📌 ملخص سريع (XPath)

    الموضوع                الصيغة                         مثال
    ---------------------------------------------------------------------
    Absolute Path           /html/...                      /html/body/div/h1
    (من أول الصفحة)

    Relative Path           //tag                          //h1
    (يدور في أي مكان)

    By Attribute            //tag[@attr='value']           //h1[@id='navbars']

    Attribute بدون قيمة    //tag[@attr]                  //input[@readonly]
    '''
    






    # close the browser
    browser.close()