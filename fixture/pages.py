from model.credLogin import LoginCred
import time
import re
from selenium.webdriver.firefox.options import Options


class Pages:

    def __init__(self, app):
        self.app = app

    def open_main_page(self):
        driver = self.app.driver
        driver.get(self.app.selectors.site_ru)

    def open_forgot_password_page(self):
        driver = self.app.driver
        driver.get(self.app.selectors.forgot_password)
        assert self.app.warning.get_outer_text(xpath=self.app.selectors.page_header_h2) == "ВОССТАНОВИТЬ ПАРОЛЬ"

    def open_cash_page(self):
        driver = self.app.driver
        self.open_main_page()
        self.app.session.login(LoginCred(username="triced ", password="TestTest12"))
        time.sleep(1)
        driver.find_element_by_xpath(self.app.selectors.cash_button).click()
        assert self.app.warning.get_outer_text(self.app.selectors.page_header_h2) == "ПОПОЛНИТЬ"

    def frame_switch(self, xpath):
        driver = self.app.driver
        driver.switch_to.frame(driver.find_element_by_xpath(xpath))

    def download_popup(self):
        options = Options()
        driver = self.app.driver
        self.open_main_page()
        driver.find_element_by_xpath(self.app.selectors.download_client_mac).click()
        options.set_preference("browser.safebrowsing.downloads.enabled", True)
        options.set_preference("browser.download.folderList", 1)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.download.dir", "/data")
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "/Users/d.demchenko/Desktop/blabla.dmg")
        time.sleep(20)

    def event_message(self, xpath):
        driver = self.app.driver

    def change_to_ru(self):
        driver = self.app.driver
        language = self.app.selectors.language
        used_language = self.app.warning.get_outer_text(language)
        if used_language == "УКР" or used_language == "ENG":
            driver.find_element_by_xpath(self.app.selectors.language).click()
            self.app.warning.wait_for_element_xpath(self.app.selectors.language_ru)
            driver.find_element_by_xpath(self.app.selectors.language_ru).click()

    #  Close Web Socket message
    def close_message(self):
        driver = self.app.driver
        driver.find_element_by_xpath(self.app.selectors.close_message).click()

    def get_user_balance(self):
        balance_string = self.app.warning.get_outer_text(self.app.selectors.balance)
        template = re.compile('([0-9]{0,3}),?([0-9]{0,3}),?([0-9]{0,3}),?.([0-9]{2})')
        match_obj = re.match(template, balance_string)

        pre_result = ''.join(match_obj.groups()[:-1])
        balance = '.'.join((pre_result, match_obj.groups()[-1:][0]))
        print(balance)
        return balance

    def open_slots_page(self):
        driver = self.app.driver
        self.open_main_page()
        driver.find_element_by_xpath(self.app.selectors.slot_button).click()
        assert driver.current_url.endswith("/games")
        assert driver.title == "games001"

    def footer_licence_info(self):
        licence_text = self.app.warning.get_outer_text(self.app.selectors.footer_licence_info)
        print(licence_text, "LolOLoLo", self.app.text.footer_licence_text)
        assert licence_text == self.app.text.footer_licence_text

