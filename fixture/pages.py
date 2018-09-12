from model.credLogin import LoginCred
import time
from selenium.webdriver.firefox.options import Options


class Pages:

    def __init__(self, app):
        self.app = app

    def open_main_page(self):
        driver = self.app.driver
        driver.get("https://beta.pokermatch.com/ru")

    def open_forgot_password_page(self):
        driver = self.app.driver
        driver.get("https://beta.pokermatch.com/ru/page/passwordreminder")
        assert self.app.warning.get_outer_text(xpath="//h2[@class='content__title']") == "ВОССТАНОВИТЬ ПАРОЛЬ"

    def open_cash_page(self):
        driver = self.app.driver
        self.open_main_page()
        self.app.session.login(LoginCred(username="triced ", password="TestTest12"))
        time.sleep(1)
        driver.find_element_by_xpath("//a[@class='button button_type_link   head__elem my_cash']").click()
        assert self.app.warning.get_outer_text("//h2[@class='content__title']") == "ИНФОРМАЦИЯ ПОЛЬЗОВАТЕЛЯ"
        self.app.warning.wait_for_element_xpath("//*[@id='cash']/iframe")

    def frame_switch(self, xpath):
        driver = self.app.driver
        driver.switch_to.frame(driver.find_element_by_xpath(xpath))

    def download_popup(self):
        options = Options()
        driver = self.app.driver
        self.open_main_page()
        driver.find_element_by_xpath("//a[@href='/download/win']/span[@class='button__inner']").click()
        options.set_preference("browser.safebrowsing.downloads.enabled", True)
        options.set_preference("browser.download.folderList", 1)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.download.dir", "/data")
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "/Users/d.demchenko/Desktop/blabla.dmg")
        time.sleep(20)