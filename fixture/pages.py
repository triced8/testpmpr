from model.credLogin import LoginCred
import time
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
