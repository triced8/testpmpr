from selenium import webdriver
import conftest
from fixture.pages import Pages
from fixture.session import SessionHelper
from fixture.registration import SignUpHelper
from fixture.admin import AdminHelper
from fixture.warningMessages import WarningMessages
from fixture.cash import Cash
from fixture.textru import TextRu

class Application:

    def __init__(self, browser):

        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "safari":
            self.driver = webdriver.Safari()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.app = conftest.app
        self.app1 = conftest.app1
        self.driver.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.registration = SignUpHelper(self)
        self.admin = AdminHelper(self)
        self.warning = WarningMessages(self)
        self.pages = Pages(self)
        self.cash = Cash(self)
        self.text = TextRu(self)


    def openMainPageRu(self):
        driver = self.driver

        #    return
        driver.get("https://beta.pokermatch.com/ru")

    # Check that fixture is valid
    def isValide(self):
        try:
            self.driver.current_url()
            return True
        except:
            return False

    # Destroy fixture
    def destroy(self):
        self.driver.quit()


