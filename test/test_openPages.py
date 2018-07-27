

def test_openNews(app):
    app.pages.openMainPage()
    app.driver.get("https://beta.pokermatch.com/uk")
    app.driver.find_element_by_xpath("//a[@class='main_menu_element news ']").click()
    assert app.warning.getOuterText("//h2[@class='content__title']") == app.text.headerNewsRu
    app.session.currentUrl(endswith="news")

def test_openTutorial(app):
    app.pages.openMainPage()
    app.driver.find_element_by_xpath("//a[@class='main_menu_element tutorial ']").click()
    assert app.warning.getOuterText("//h2[@class='content__title']") == app.text.headerTutorialRu
    app.session.currentUrl(endswith="tutorial")

def test_openPromo(app):
    app.pages.openMainPage()
    app.driver.find_element_by_xpath("//a[@class='main_menu_element promo ']").click()
    assert app.warning.getOuterText("//h2[@class='content__title']") == app.text.headerPromoRu
    app.session.currentUrl(endswith="promo")

def test_openAbout(app):
    app.pages.openMainPage()
    app.driver.find_element_by_xpath("//a[@class='main_menu_element about ']").click()
    assert app.warning.getOuterText("//h2[@class='content__title']") == app.text.headerAboutRu
    app.session.currentUrl(endswith="about")

"""# Только на проде
def test_openPaymants(app):
    app.pages.openMainPage()
    app.driver.find_element_by_xpath("//a[@class='main_menu_element payments  ']").click()
    assert app.warning.getOuterText("//article[@class='news_wrapper']//h3") == app.text.headerPaymantsRu
    app.session.currentUrl(endswith="payments")
"""
