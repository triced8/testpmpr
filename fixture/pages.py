from model.credLogin import LoginCred
import time


class Pages:

    def __init__(self, app):
        self.app = app

    def openMainPage(self):
        driver = self.app.driver
        driver.get("https://beta.pokermatch.com/ru")

    def openForgotPasswordPage(self):
        driver = self.app.driver
        driver.get("https://beta.pokermatch.com/ru/page/passwordreminder")
        assert self.app.warning.getOuterText(xpath="//h2[@class='content__title']") == "ВОССТАНОВИТЬ ПАРОЛЬ"

    def openCahsPage(self):
        driver = self.app.driver
        self.openMainPage()
        self.app.session.login(LoginCred(username="triced ", password="TestTest12"))
        time.sleep(1)
        driver.find_element_by_xpath("//a[@class='button button_type_link   head__elem my_cash']").click()
        assert self.app.warning.getOuterText("//h2[@class='content__title']") == "ИНФОРМАЦИЯ ПОЛЬЗОВАТЕЛЯ"
        self.app.warning.waitForElementXpath("//*[@id='cash']/iframe")

    def frameSwitch(self, xpath):
        driver = self.app.driver
        driver.switch_to.frame(driver.find_element_by_xpath(xpath))
