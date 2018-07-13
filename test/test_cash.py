from random import randrange
import time
from model.credLogin import LoginCred

random = randrange(100000000)



def test_openCasgPage(app):
    app.pages.openCahsPage()
    app.pages.frameSwitch("//*[@id='cash']/iframe")
    assert app.warning.getOuterText("//ul[@class='filter top_menu']/li[1]") == "Пополнить счет"
    app.pages.openMainPage()
    app.session.logout()


def test_openCardForm(app):
    app.pages.openCahsPage()
    app.pages.frameSwitch("//*[@id='cash']/iframe")
    app.driver.find_element_by_xpath("//div[@class ='widget deposit_widget']").click()
    #time.sleep(3)
    if app.session.elementIsDisplay("//label[@for='stored_card']"):
        app.driver.find_element_by_xpath("//label[@for='new_card']").click()
    app.warning.waitForElementXpath("//div[@class='card_face zf-changed']")
    assert app.session.elementIsDisplay("//div[@class='card_face zf-changed']")
    assert app.warning.getOuterText("//label[.='Номер карты']") == "НОМЕР КАРТЫ"
    app.pages.openMainPage()
    app.session.logout()


def test_fillCardForm(app):
    app.pages.openCahsPage()
    app.pages.frameSwitch("//*[@id='cash']/iframe")
    app.driver.find_element_by_xpath("//div[@class ='widget deposit_widget']").click()
    time.sleep(3)
    if app.session.elementIsDisplay("//label[@for='stored_card']"):
        app.driver.find_element_by_xpath("//label[@for='new_card']").click()
        time.sleep(0.5)
    assert app.session.elementIsDisplay("//div[@class='card_face zf-changed']")
    assert app.warning.getOuterText("//label[.='Номер карты']") == "НОМЕР КАРТЫ"
    app.cash.fillCardForm()
    app.pages.openMainPage()
    app.session.logout()

def test_openGameClient(app):
    app.pages.openMainPage()
    app.session.login(LoginCred(username="triced", password="TestTest12"))
    time.sleep(0.2)
    app.driver.find_element_by_xpath("//div[@class='top_menu_buttons']//span[@class='button__inner']").click()
    time.sleep(2)
    app.driver.switch_to_window(app.driver.window_handles[1])
    assert app.driver.title.startswith('PokerMatch Лобби | Ник: triced |')