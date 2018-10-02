import pytest


@pytest.allure.step("Open news page")
def test_open_news(app):
    with pytest.allure.step("Open main page"):
        app.pages.open_main_page()
    with pytest.allure.step("Click on the 'news' link at the header menu"):
        app.driver.find_element_by_xpath(app.selectors.header_menu_news).click()
    with pytest.allure.step("Assert for name of page"):
        assert app.warning.get_outer_text(app.selectors.page_header_h2) == app.text.headerNewsRu
    with pytest.allure.step("Assert for endswith URL"):
        app.session.current_url(endswith="news")


@pytest.allure.step("Open tutorial page")
def test_open_tutorial(app):
    with pytest.allure.step("Open main page"):
        app.pages.open_main_page()
    with pytest.allure.step("Click on the 'tutorial' link at the header menu"):
        app.driver.find_element_by_xpath(app.selectors.header_menu_tutorial).click()
    with pytest.allure.step("Assert for name of page"):
        assert app.warning.get_outer_text(app.selectors.page_header_h2) == app.text.headerTutorialRu
    with pytest.allure.step("Assert for endswith URL"):
        app.session.current_url(endswith="tutorial")


@pytest.allure.step("Open promo page")
def test_open_promo(app):
    with pytest.allure.step("Open main page"):
        app.pages.open_main_page()
    with pytest.allure.step("Click on the 'promo' link at the header menu"):
        app.driver.find_element_by_xpath(app.selectors.header_menu_promo).click()
    with pytest.allure.step("Assert for name of page"):
        assert app.warning.get_outer_text(app.selectors.page_header_h2) == app.text.headerPromoRu
    with pytest.allure.step("Assert for endswith URL"):
        app.session.current_url(endswith="promo")


@pytest.allure.step("Open about page")
def test_open_about(app):
    with pytest.allure.step("Open main page"):
        app.pages.open_main_page()
    with pytest.allure.step("Click on the 'about' link at the header menu"):
        app.driver.find_element_by_xpath(app.selectors.header_menu_about).click()
    with pytest.allure.step("Assert for name of page"):
        assert app.warning.get_outer_text(app.selectors.page_header_h2) == app.text.headerAboutRu
    with pytest.allure.step("Assert for endswith URL"):
        app.session.current_url(endswith="about")


"""# Только на проде
def test_open_payments(app):
    app.pages.openMainPage()
    app.driver.find_element_by_xpath(app.selectors.header_menu_payments).click()
    assert app.warning.getOuterText("//article[@class='news_wrapper']//h3") == app.text.headerPaymantsRu
    app.session.currentUrl(endswith="payments")
"""
