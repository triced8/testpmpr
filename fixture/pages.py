from model.credLogin import LoginCred
import time
import re
from selenium.webdriver.firefox.options import Options
import pytest

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

    def change_to_ua(self):
        driver = self.app.driver
        language = self.app.selectors.language
        used_language = self.app.warning.get_outer_text(language)
        if used_language == "РУС" or used_language == "ENG":
            driver.find_element_by_xpath(self.app.selectors.language).click()
            self.app.warning.wait_for_element_xpath(self.app.selectors.language_ua)
            driver.find_element_by_xpath(self.app.selectors.language_ua).click()

    def change_to_en(self):
        driver = self.app.driver
        language = self.app.selectors.language
        used_language = self.app.warning.get_outer_text(language)
        if used_language == "РУС" or used_language == "УКР":
            driver.find_element_by_xpath(self.app.selectors.language).click()
            self.app.warning.wait_for_element_xpath(self.app.selectors.language_en)
            driver.find_element_by_xpath(self.app.selectors.language_en).click()

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
        print(licence_text, "LolOLoLo\n", self.app.text.footer_licence_text)
        assert licence_text == self.app.text.footer_licence_text

    def open_news_page(self):
        self.app.pages.open_main_page()
        self.app.driver.find_element_by_xpath(self.app.selectors.header_menu_news).click()
        assert self.app.warning.get_outer_text(self.app.selectors.page_header_h2) == self.app.text.header_news_ru
        self.app.session.current_url(endswith="news")

    def open_tutorial_page(self):
        app = self.app
        app.pages.open_main_page()
        app.driver.find_element_by_xpath(app.selectors.header_menu_tutorial).click()
        assert app.warning.get_outer_text(app.selectors.page_header_h2) == app.text.header_tutorial_ru
        app.session.current_url(endswith="tutorial")

    def open_promo_page(self):
        app = self.app
        app.pages.open_main_page()
        app.driver.find_element_by_xpath(app.selectors.header_menu_promo).click()
        assert app.warning.get_outer_text(app.selectors.page_header_h2) == app.text.header_promo_ru
        app.session.current_url(endswith="promo")

    def open_about_page(self):
        app = self.app
        app.pages.open_main_page()
        app.driver.find_element_by_xpath(app.selectors.header_menu_about).click()
        assert app.warning.get_outer_text(app.selectors.page_header_h2) == app.text.header_about_ru
        app.session.current_url(endswith="about")

    def open_terms_and_conditions_page(self):
        self.app.pages.open_main_page()
        self.app.driver.find_element_by_xpath(self.app.selectors.footer_terms_and_conditions).click()
        assert self.app.warning.get_outer_text(self.app.selectors.page_header_h2) == self.app.text.header_terms_and_conditions_ru
        self.app.session.current_url(endswith="termsandconditions")

    def open_privacy_policy_page(self):
        self.app.pages.open_main_page()
        self.app.driver.find_element_by_xpath(self.app.selectors.footer_privacy_policy).click()
        assert self.app.warning.get_outer_text(
            self.app.selectors.page_header_h2) == self.app.text.header_privacy_policy_ru
        self.app.session.current_url(endswith="privacypolicy")

    def open_antifraud_page(self):
        self.app.pages.open_main_page()
        self.app.driver.find_element_by_xpath(self.app.selectors.footer_antifraud).click()
        assert self.app.warning.get_outer_text(
            self.app.selectors.page_header_h2) == self.app.text.header_antifraud
        self.app.session.current_url(endswith="antifraud")

    def open_contacts_page(self):
        self.app.pages.open_main_page()
        self.app.driver.find_element_by_xpath(self.app.selectors.footer_contacts).click()
        assert self.app.warning.get_outer_text(
            self.app.selectors.page_header_h2) == self.app.text.header_about_ru
        self.app.session.current_url(endswith="/about/contacts")

    @pytest.allure.step("Open news page")
    def check_news_page_local(self):
        with pytest.allure.step("Create dict with texts"):
            locale_switcher = dict(
                ru=self.app.text.header_news_ru,
                en=self.app.text.header_news_en,
                ua=self.app.text.header_news_ua
            )
        with pytest.allure.step("Open main page"):
            self.app.pages.open_main_page()
        with pytest.allure.step("Open News page"):
            self.app.driver.find_element_by_xpath(self.app.selectors.header_menu_news).click()
        with pytest.allure.step("Create cycle for check different language from dict"):
            for k, v in locale_switcher.items():
                locale_point = v
                with pytest.allure.step("Change in to needed language"):
                    if v == self.app.text.header_news_ru:
                        self.change_to_ru()
                        time.sleep(0.3)
                    elif v == self.app.text.header_news_en:
                        self.change_to_en()
                        time.sleep(0.3)
                    elif v == self.app.text.header_news_ua:
                        self.change_to_ua()
                        time.sleep(0.3)
                with pytest.allure.step("Check that header in needed localization"):
                    assert self.app.warning.get_outer_text(self.app.selectors.page_header_h2) == locale_point
                with pytest.allure.step("Check that URL endswith"):
                    self.app.session.current_url(endswith="news")

    def check_tutorial_page_local(self):
        locale_switcher = dict(
            ru=self.app.text.header_tutorial_ru,
            en=self.app.text.header_tutorial_en,
            ua=self.app.text.header_tutorial_ua
        )
        self.app.pages.open_main_page()
        self.app.driver.find_element_by_xpath(self.app.selectors.header_menu_tutorial).click()
        for k, v in locale_switcher.items():
            locale_point = v

            if v == self.app.text.header_tutorial_ru:
                self.change_to_ru()
                time.sleep(0.3)
            elif v == self.app.text.header_tutorial_en:
                self.change_to_en()
                time.sleep(0.3)
            elif v == self.app.text.header_tutorial_ua:
                self.change_to_ua()
                time.sleep(0.3)
            assert self.app.warning.get_outer_text(self.app.selectors.page_header_h2) == locale_point
            self.app.session.current_url(endswith="tutorial")

    def check_promo_page_local(self):
        locale_switcher = dict(
            ru=self.app.text.header_promo_ru,
            en=self.app.text.header_promo_en,
            ua=self.app.text.header_promo_ua
        )
        self.app.pages.open_main_page()
        self.app.driver.find_element_by_xpath(self.app.selectors.header_menu_promo).click()
        for k, v in locale_switcher.items():
            locale_point = v

            if v == self.app.text.header_promo_ru:
                self.change_to_ru()
                time.sleep(0.3)
            elif v == self.app.text.header_promo_en:
                self.change_to_en()
                time.sleep(0.3)
            elif v == self.app.text.header_promo_ua:
                self.change_to_ua()
                time.sleep(0.3)
            assert self.app.warning.get_outer_text(self.app.selectors.page_header_h2) == locale_point
            self.app.session.current_url(endswith="promo")

    def check_about_page_local(self):
        locale_switcher = dict(
            ru=self.app.text.header_about_ru,
            en=self.app.text.header_about_en,
            ua=self.app.text.header_about_ua
        )
        self.app.pages.open_main_page()
        self.app.driver.find_element_by_xpath(self.app.selectors.header_menu_about).click()
        for k, v in locale_switcher.items():
            locale_point = v

            if v == self.app.text.header_about_ru:
                self.change_to_ru()
                time.sleep(0.3)
            elif v == self.app.text.header_about_en:
                self.change_to_en()
                time.sleep(0.3)
            elif v == self.app.text.header_about_ua:
                self.change_to_ua()
                time.sleep(0.3)
            assert self.app.warning.get_outer_text(self.app.selectors.page_header_h2) == locale_point
            self.app.session.current_url(endswith="about")