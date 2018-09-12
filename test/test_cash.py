from random import randrange
import time
from model.credLogin import LoginCred
import pytest

random = randrange(100000000)


@pytest.allure.step("Open cash page")
def test_open_cash_page(app):
    with pytest.allure.step("Open Cash page"):
        app.pages.open_cash_page()
    with pytest.allure.step("Switch in to the cash frame"):
        app.pages.frame_switch("//*[@id='cash']/iframe")
    with pytest.allure.step("Assert that page is opened"):
        assert app.warning.get_outer_text("//ul[@class='filter top_menu']/li[1]") == app.text.headerCash
    with pytest.allure.step("Logout from user account"):
        app.pages.open_main_page()
        app.session.logout()


@pytest.allure.step("Open cash form")
def test_open_card_form(app):
    with pytest.allure.step("Open Cash page"):
        app.pages.open_cash_page()
    with pytest.allure.step("Switch in to the cash frame"):
        app.pages.frame_switch("//*[@id='cash']/iframe")
    with pytest.allure.step("Open cash form"):
        app.driver.find_element_by_xpath("//div[@class ='widget deposit_widget']").click()
    # time.sleep(3)
    with pytest.allure.step("If user have saved cards, open form"):
        if app.session.element_is_display("//label[@for='stored_card']"):
            app.driver.find_element_by_xpath("//label[@for='new_card']").click()
    with pytest.allure.step("Check fields "):
        app.warning.wait_for_element_xpath("//div[@class='card_face zf-changed']")
        assert app.session.element_is_display("//div[@class='card_face zf-changed']")
        assert app.warning.get_outer_text("//label[.='Номер карты']") == "НОМЕР КАРТЫ"
    with pytest.allure.step("Logout from user account"):
        app.pages.open_main_page()
        app.session.logout()


@pytest.allure.step("Fill cash from with valid data")
def test_fill_card_form(app):
    with pytest.allure.step("Open Cash page"):
        app.pages.open_cash_page()
    with pytest.allure.step("Switch in to the cash frame"):
        app.pages.frame_switch("//*[@id='cash']/iframe")
    with pytest.allure.step("Open cash form"):
        app.driver.find_element_by_xpath("//div[@class ='widget deposit_widget']").click()
    # time.sleep(3)
    with pytest.allure.step("If user have saved cards, open form"):
        if app.session.element_is_display("//label[@for='stored_card']"):
            app.driver.find_element_by_xpath("//label[@for='new_card']").click()
    with pytest.allure.step("Check fields "):
        app.warning.wait_for_element_xpath("//div[@class='card_face zf-changed']")
        assert app.session.element_is_display("//div[@class='card_face zf-changed']")
        assert app.warning.get_outer_text("//label[.='Номер карты']") == "НОМЕР КАРТЫ"
    with pytest.allure.step("Fill in card's form"):
        app.cash.fill_card_form()
    with pytest.allure.step("Logout from user account"):
        app.pages.open_main_page()
        app.session.logout()
    app.cash.fill_card_form()


@pytest.allure.step("Open poker client")
def test_open_game_client(app):
    with pytest.allure.step("Open main page"):
        app.pages.open_main_page()
    with pytest.allure.step("LogIn"):
        app.session.login(LoginCred(username="triced", password="TestTest12"))
        time.sleep(0.2)
    with pytest.allure.step("Open game's client"):
        app.driver.find_element_by_xpath("//div[@class='top_menu_buttons']//span[@class='button__inner']").click()
        time.sleep(2)
    with pytest.allure.step("Switch at the web games's client page"):
        app.driver.switch_to_window(app.driver.window_handles[1])
    with pytest.allure.step("Check Nick name and title"):
        assert app.driver.title.startswith('PokerMatch Лобби | Ник: triced |')
    with pytest.allure.step("Switch to sate"):
        app.driver.switch_to_window(app.driver.window_handles[0])
    with pytest.allure.step("Logout from user account"):
        app.session.logout()
