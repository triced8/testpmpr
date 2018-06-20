from selenium import webdriver

import conftest
from fixture.session import SessionHelper
from fixture.registration import SignUpHelper
from fixture.admin import AdminHelper


class Application:

    def __init__(self):
        self.app = conftest.app
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.registration = SignUpHelper(self)
        self.admin = AdminHelper(self)


    def openMainPage(self):
        driver = self.driver
        driver.get("https://beta.pokermatch.com/ru")

    #Chack that fixture is valide
    def isValide(self):
        try:
            self.driver.current_url()
            return True
        except:
            return False
    #Destroy fixture
    def destroy(self):
        self.driver.quit()
