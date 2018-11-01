class Selectors:

    def __init__(self, app):
        self.app = app

    #  URL
    site_ru = "https://beta.pokermatch.com/ru"
    site_admin = "https://beta.pokermatch.com/sa"
    forgot_password = "https://beta.pokermatch.com/ru/page/passwordreminder"

    # Header menu links
    header_menu_news = "//a[@class='main_menu_element news ']"  # News
    header_menu_tutorial = "//a[@class='main_menu_element tutorial ']"  # How to play
    header_menu_promo = "//a[@class='main_menu_element promo ']"  # Promo/Акции
    header_menu_about = "//a[@class='main_menu_element about ']"  # About
    header_menu_payments = "//a[@class='main_menu_element payments  ']"  # Payments/Платежи
    language = "//div[@id = 'languages']"  # language button
    language_ru = "//span[contains(text(),'Рус')]"  # Rus language button from the drop-dawn lang's list
    language_en = "//span[contains(text(),'Укр')]"   # Eng language button from the drop-dawn lang's list
    language_ua = "//span[contains(text(),'Eng')]"   # Укр language button from the drop-dawn lang's list
    balance = "//span[@id='balance']"
    slot_button = "//a[@href='/ru/games']"
    poker_button = "//a[@class='info-list__item-value']"

    # Headers of information pages
    page_header_h2 = "//h2[@class='content__title']"

    # Buttons
    cash_button = "//a[@class='button button_type_link   head__elem my_cash']"  # Cash button at the header
    download_client_mac = "//a[@class='desktop-client']"  # Download link at the banner
    signup_button = "//div[@class='head__inner']/div[2]/a[1]" # Signup button at the header
    signup_button_form = "//div[@id='registration']/div/div/div[2]/form/button/div"  # Signup button at the signup form
    login_button = "//a[@href='#login']/span[@class='button__inner']"  # Login button at the header
    login_button_form = "//form[@action='/login/']//div[@class='modala-button__text']"  # Login button at the signup form
    logout_button = "//a[@href='/logout/']"  # Logout button at the header

    # Signup fields at the Signup form
    signup_password_field = "(//input[@name='password'])[4]"
    captcha_field = "(//input[@name='captcha'])[2]"
    email_filed = "email"  # By filed's name
    nick_name_filed = "nick"  # By field's name
    nick_name_success = "//span[@class='modala__ok']"
    nick_name_boarder_success = "//div[@id='registration']//input[@id='login']"
    see_password_button = "//div[@id='registration']//span[@class='switch_pass']"
    signup_h4_title = "//div[@id='registration']//h4[@class='modala__title']"

    # Login fields at the Login form
    login_field = "login"  # By field's name
    login_password_field = "(//input[@name='password'])[2]"  # Password field at the login form

    # Cash page UAH
    paymega_uah_cashin_button = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__table_col'][1]//button"  # PayMega chain button
    ecommpay_uah_cashin_button = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__table_col'][1]//button"  # Ecommpay chain button
    ecommpay_uah_cashin_button_2 = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__table_col'][2]//button"  # Ecommpay chain button
    alfa_uah_cashin_button = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__table_col'][2]//button"  # Alfa Click button
    psb_uah_cashin_button = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__table_col'][3]//button"  # Prom Sv Bank chain button
    wm_uah_cashin_button = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__table_col'][4]//button"  # Web Money chain button
    qiwi_uah_cashin_button = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__table_col'][5]//button"  # QIWI chain button
    skrill_uah_cashin_button = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__table_col'][6]//button"  # Skrill chain button
    neteller_uah_cashin_button = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__table_col'][7]//button"  # Neteller chain button
    yandex_uah_cashin_button = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__table_col'][8]//button"  # Yandex chain button
    ks_uah_cashin_button = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__table_col'][9]//button"  # KievStar chain button
    life_uah_cashin_button = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__table_col'][10]//button"  # Life chain button
    privat_uah_cashin_button = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__table_col'][11]//button"  # Privat24 chain button
    terminal_uah_cashin_button = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__table_col'][12]//button"  # Terminal chain button
    cash_button_ua_list = [paymega_uah_cashin_button, ecommpay_uah_cashin_button, alfa_uah_cashin_button,
                           psb_uah_cashin_button, wm_uah_cashin_button, qiwi_uah_cashin_button, skrill_uah_cashin_button,
                           neteller_uah_cashin_button, yandex_uah_cashin_button, privat_uah_cashin_button]

    # Cash fields at the inner frame
    paymega_cash_field = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__content'][1]//div[@class='content_fields']/input"  # PayMega
    ecommpay_cash_field = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__content'][2]//div[@class='content_fields']"  # Ecommpay
    c = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__content'][3]//div[@class='content_fields']"
    d = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__content'][4]//div[@class='content_fields']"
    e = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__content'][5]//div[@class='content_fields']"
    f = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__content'][6]//div[@class='content_fields']"
    g = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__content'][7]//div[@class='content_fields']"
    h = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__content'][8]//div[@class='content_fields']"
    i = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__content'][9]//div[@class='content_fields']"
    j = "//div[@class='pm_cash__table pm_cash__table_in']//div[@class='pm_cash__content'][10]//div[@class='content_fields']"
    cash_field_list = [paymega_cash_field, ecommpay_cash_field, c, d, e, f, g, h, i, j]
    test_ec = "//div[@class='pm_cash__table pm_cash__table_in']/div[3]//form[@class='pm_cash__left']//button[@type='submit']/span[@class='button__inner']"

    # Cash inner fields
    ecommpay_inner_cash_button = "//div[@class='pm_cash__table pm_cash__table_in']/div[5]//button[@type='submit']/span[@class='button__inner']"

    # Event messages
    event_message = "//div[@class='event_message']"
    close_message = "//div[@class='close_message websymbol']"

    # Footer
    footer_licence_info = "//div[@class='footer_licence_info']"
    footer_terms_and_conditions = "//a[@href='/ru/termsandconditions']"
    footer_privacy_policy = "//a[@href='/ru/privacypolicy']"
    footer_antifraud = "//a[@href='/ru/antifraud']"
    footer_contacts = "//a[@href='/ru/about/contacts']"