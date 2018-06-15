from selenium import webdriver
from fixture.session import SessionHelper
from fixture.registration import SignUpHelper
from fixture.admin import AdminHelper

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.registration = SignUpHelper(self)
        self.admin = AdminHelper(self)

    def openMainPage(self):
        driver = self.driver
        driver.get("https://beta.pokermatch.com/ru")



    def destroy(self):
        self.driver.quit()


