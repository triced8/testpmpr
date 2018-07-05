from fixture.warningMessages import WarningMessages

class Pages:

    def __init__(self, app):
        self.app = app


    def openForgotPasswordPage(self):
        driver = self.app.driver
        driver.get("https://beta.pokermatch.com/ru/page/passwordreminder")
        assert self.app.warning.getOuterText(xpath="//h2[@class='content__title']") == "ВОССТАНОВИТЬ ПАРОЛЬ"

