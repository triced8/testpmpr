import pytest


@pytest.allure.step("Open news page")
def test_open_news(app):
    with pytest.allure.step("Open main page"):
        app.pages.open_main_page()
    with pytest.allure.step("Click on the 'news' link at the header menu"):
        app.driver.find_element_by_xpath(app.selectors.header_menu_news).click()
    with pytest.allure.step("Assert for name of page"):
        assert app.warning.get_outer_text(app.selectors.page_header_h2) == app.text.header_news_ru
    with pytest.allure.step("Assert for endswith URL"):
        app.session.current_url(endswith="news")


@pytest.allure.step("Open tutorial page")
def test_open_tutorial(app):
    with pytest.allure.step("Open main page"):
        app.pages.open_main_page()
    with pytest.allure.step("Click on the 'tutorial' link at the header menu"):
        app.driver.find_element_by_xpath(app.selectors.header_menu_tutorial).click()
    with pytest.allure.step("Assert for name of page"):
        assert app.warning.get_outer_text(app.selectors.page_header_h2) == app.text.header_tutorial_ru
    with pytest.allure.step("Assert for endswith URL"):
        app.session.current_url(endswith="tutorial")


@pytest.allure.step("Open promo page")
def test_open_promo(app):
    with pytest.allure.step("Open main page"):
        app.pages.open_main_page()
    with pytest.allure.step("Click on the 'promo' link at the header menu"):
        app.driver.find_element_by_xpath(app.selectors.header_menu_promo).click()
    with pytest.allure.step("Assert for name of page"):
        assert app.warning.get_outer_text(app.selectors.page_header_h2) == app.text.header_promo_ru
    with pytest.allure.step("Assert for endswith URL"):
        app.session.current_url(endswith="promo")


@pytest.allure.step("Open about page")
def test_open_about(app):
    with pytest.allure.step("Open main page"):
        app.pages.open_main_page()
    with pytest.allure.step("Click on the 'about' link at the header menu"):
        app.driver.find_element_by_xpath(app.selectors.header_menu_about).click()
    with pytest.allure.step("Assert for name of page"):
        assert app.warning.get_outer_text(app.selectors.page_header_h2) == app.text.header_about_ru
    with pytest.allure.step("Assert for endswith URL"):
        app.session.current_url(endswith="about")


@pytest.allure.step("Open about page")
def test_open_header_links(app):
    with pytest.allure.step("Open main page"):
        app.open_main_page_ru()
    with pytest.allure.step("Change in to Ru local if it needed"):
        app.pages.change_to_ru()
    with pytest.allure.step("Open news page"):
        app.pages.open_news_page()
    with pytest.allure.step("Open tutorial page"):
        app.pages.open_tutorial_page()
    with pytest.allure.step("Open promo page"):
        app.pages.open_promo_page()
    with pytest.allure.step("Open about page"):
        app.pages.open_about_page()


@pytest.allure.step("Open footer links")
def test_open_footer_links(app):
    with pytest.allure.step("Open main page"):
        app.open_main_page_ru()
    with pytest.allure.step("Open 'terms and conditions' page"):
        app.pages.open_terms_and_conditions_page()
    with pytest.allure.step("Open 'privacy policy' page"):
        app.pages.open_privacy_policy_page()
    with pytest.allure.step("Open 'antifraud' page"):
        app.pages.open_antifraud_page()
    with pytest.allure.step("Open 'contacts' page"):
        app.pages.open_contacts_page()



def test_open_news1(app):
    with pytest.allure.step("Check News Page"):
        app.pages.check_news_page_local()
    with pytest.allure.step("Check Tutorial Page"):
        app.pages.check_tutorial_page_local()
    with pytest.allure.step("Open Promo page"):
        app.pages.check_promo_page_local()
    with pytest.allure.step("Open About page"):
        app.pages.check_about_page_local()

"""# Только на проде
def test_open_payments(app):
    app.pages.openMainPage()
    app.driver.find_element_by_xpath(app.selectors.header_menu_payments).click()
    assert app.warning.getOuterText("//article[@class='news_wrapper']//h3") == app.text.headerPaymantsRu
    app.session.currentUrl(endswith="payments")
"""
