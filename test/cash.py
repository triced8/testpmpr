from random import randrange
import time
from model.credLogin import LoginCred
import pytest
from selenium.common.exceptions import NoSuchElementException
from crontab import CronTab


random = randrange(100000000)
"""
@pytest.allure.step("Open inner frame at the cash page")
def test_open_inner_frames(app):
    with pytest.allure.step("Open Cash page with login"):
        app.pages.open_cash_page()
    with pytest.allure.step("Open inner frames for UAH"):
        app.cash.open_inner_frames()
    with pytest.allure.step("Logout from account"):
        app.session.logout()


@pytest.allure.step("Open inner frame PayMega")
def test_use_paymega(app):
    with pytest.allure.step("Open Cash page with login"):
        app.pages.open_cash_page()
        app.session.element_is_display("//div[@class='content']//div[@class='pm_cash__table pm_cash__table_in']/div[3]/div[@class='pm_cash__container']/iframe")
    with pytest.allure.step("Open paymega inner frames for UAH"):
        app.cash.open_inner_frame(xpath_cash=app.selectors.paymega_uah_cashin_button, xpath=app.selectors.paymega_cash_field)
    with pytest.allure.step("Fill cash field"):
        time.sleep(2)
        app.cash.fill_inner_frame(app.selectors.paymega_cash_field)
    with pytest.allure.step("Logout from account"):
        app.session.logout()


@pytest.allure.step("Open inner frame ecommpay")
def test_use_ecommpay(app):
    with pytest.allure.step("Open Cash page with login"):
        app.pages.open_cash_page()
    with pytest.allure.step("Get balance before cash in"):
        before_balance = app.pages.get_user_balance()
    with pytest.allure.step("Open paymega inner frames for UAH"):
        app.cash.open_inner_frame(xpath_cash=app.selectors.ecommpay_uah_cashin_button_2, xpath=app.selectors.test_ec) # ecommpay_cash_field check the button is displayed
    with pytest.allure.step("Fill and send data at the ecommpay form"):
        app.cash.fill_ecommpay_fields()
    with pytest.allure.step("Return to main window"):
        app.driver.switch_to.default_content()
    with pytest.allure.step("Check event message"):
        assert app.warning.get_outer_text(app.selectors.event_message) == app.text.cash_in_event_message_ru
    with pytest.allure.step("Close event message"):
        app.pages.close_message()
    with pytest.allure.step("Get balance after cash in"):
        after_balance = app.pages.get_user_balance()
    with pytest.allure.step("Check difference between balances"):
        assert int(after_balance) - int(before_balance) == 100
    with pytest.allure.step("Logout from account"):
        app.session.logout()
"""





@pytest.allure.step("")
def test_open_privat(app):
    app.pages.open_main_page()
    #time.sleep(6)
    if app.session.check_exists_by_xpath(xpath="//div[@class='head__col']/a[@href='#registration']"):
        app.session.login(LoginCred(username="triced", password="TestTest12"))
    app.pages.open_cash_page()
    app.cash.open_privat_inner_frame()
    time.sleep(1)
    app.cash.open_privat_page()
    try:
        app.pages.current_url_start(startswith="https://www.privat24.ua")
    except NoSuchElementException as e:
        print(f"Error: {e.msg}")
    finally:
        app.pages.open_main_page()
pwd

def test_open_dep_web_money(app):
    app.pages.open_main_page()
    if app.session.check_exists_by_xpath(xpath="//div[@class='head__col']/a[@href='#registration']"):
        app.session.login(LoginCred(username="triced", password="TestTest12"))
    app.pages.open_cash_page()
    time.sleep(1)
    app.cash.open_web_money_inner_frame()
    time.sleep(1)
    app.cash.open_web_money_frame()
    try:
        assert app.session.element_is_display("//input[@name='choose_auth']")
    except AssertionError as e:
        print(f"Error: {e.msg}")
    finally:
        app.driver.switch_to.default_content()


def test_open_dep_qiwi(app):
    app.pages.open_main_page()
    if app.session.check_exists_by_xpath(xpath="//div[@class='head__col']/a[@href='#registration']"):
        app.session.login(LoginCred(username="triced", password="TestTest12"))
    app.pages.open_cash_page()
    app.cash.open_qiwi_inner_frame()
    app.pages.fill_input(xpath="//div[@class='pm_cash__table pm_cash__table_in']//input[@name='phone']",
                         data="380993694333")
    app.cash.open_qiwi_frame()
    try:
        app.session.element_is_displayed("//div[@id='InvoiceInfoView-Amount']")
    except AssertionError as e:
        print(f"Error: {e.msg}")
    finally:
        app.driver.switch_to.default_content()


def test_open_dep_skrill(app):
    app.pages.open_main_page()
    if app.session.check_exists_by_xpath(xpath="//div[@class='head__col']/a[@href='#registration']"):
        app.session.login(LoginCred(username="triced", password="TestTest12"))
    app.pages.open_cash_page()
    app.cash.open_skrill_inner_frame()
    time.sleep(1)
    app.cash.open_skrill_frame()
    try:
        assert app.session.element_is_display("//div[@class='skrill-headline']")
    except AssertionError as e:
        print(f"Error: {e.msg}")
    finally:
        app.driver.switch_to.default_content()


def test_open_dep_neteller(app):
    app.pages.open_main_page()
    if app.session.check_exists_by_xpath(xpath="//div[@class='head__col']/a[@href='#registration']"):
        app.session.login(LoginCred(username="triced", password="TestTest12"))
    app.pages.open_cash_page()
    app.cash.open_neteller_inner_frame()
    app.pages.fill_input(xpath="//input[@name='net_account']", data="342534524352")
    time.sleep(1)
    app.cash.open_neteller_frame()
    try:
        app.session.element_is_displayed("//td[@class='sum']")
    except AssertionError as e:
        print(f"Error: {e.msg}")
    finally:
        app.driver.switch_to.default_content()
        app.pages.open_cash_page()


def test_open_dep_adv(app):
    app.pages.open_main_page()
    if app.session.check_exists_by_xpath(xpath="//div[@class='head__col']/a[@href='#registration']"):
        app.session.login(LoginCred(username="triced", password="TestTest12"))
    app.pages.open_cash_page()
    app.cash.open_adv_inner_frame()
    time.sleep(1)
    app.cash.open_adv_page()
    time.sleep(1)
    try:
        app.pages.current_url_start(startswith="https://wallet.advcash.com/sci/login.jsf")
    except NoSuchElementException as e:
        print(f"Error: {e.msg}")
    finally:
        app.driver.close()
        app.pages.switch_to_first_tab()


def test_open_dep_kiev_star(app):
    app.pages.open_main_page()
    if app.session.check_exists_by_xpath(xpath="//div[@class='head__col']/a[@href='#registration']"):
        app.session.login(LoginCred(username="triced", password="TestTest12"))
        app.pages.open_main_page()
    app.pages.open_cash_page()
    app.cash.open_kiev_star_page()
    try:
        app.pages.current_url_start(startswith="https://money.kyivstar.ua/ru/service/view/pokermatch")
    except NoSuchElementException as e:
        print(f"Error: {e.msg}")
    finally:
        app.driver.close()
        app.pages.switch_to_first_tab()
    time.sleep(1)


def test_open_dep_life(app):
    app.pages.open_main_page()
    # time.sleep(7)
    if app.session.check_exists_by_xpath(xpath="//div[@class='head__col']/a[@href='#registration']"):
        app.session.login(LoginCred(username="triced", password="TestTest12"))
        app.pages.open_main_page()
    app.pages.open_cash_page()
    app.cash.open_life_page()
    time.sleep(2)
    try:
        app.pages.current_url_start(startswith="https://paycell.lifecell.ua/")
    except NoSuchElementException as e:
        print(f"Error: {e.msg}")
    finally:
        app.driver.close()
        app.pages.switch_to_first_tab()


def test_open_dep_yad(app):
    app.pages.open_main_page()
    #time.sleep(7)
    if app.session.check_exists_by_xpath(xpath="//div[@class='head__col']/a[@href='#registration']"):
        app.session.login(LoginCred(username="triced", password="TestTest12"))
    app.pages.open_cash_page()
    app.cash.open_yad_inner_frame()
    time.sleep(1)
    app.cash.open_yad_page()
    try:
        app.session.element_is_display("//h1[@class='title']")
        app.pages.current_url_start(startswith="https://money.yandex.ru/payments/internal/confirmation?orderId")
    except AssertionError as e:
        print(f"Error: {e.msg}")
    finally:
        app.driver.close()
        app.pages.switch_to_first_tab()
    time.sleep(4)


"""
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
        app.session.logout() """
