#from model.credLogin import LoginCred
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from fixture.session import SessionHelper

class WarningMessages:

    def __init__(self, app):
        self.app = app

    def warrningMessageFromLoginPopUp(self):
        waitElement = self.waitForElementXpath("(//input[@name='password'])[2]/following::div[1]")
        message = waitElement.get_attribute("outerText")
        return message

    def warrningBoarderPasswordField(self):
        waitElement = self.waitForElementXpath("//div[@id='login']//input[@name='password'][2]")
        border = waitElement.value_of_css_property("border-bottom-color")
        return border

    def passswordFieldGetValue(self):
        waitElement = self.waitForElementXpath("(//input[@name='password'])[2]")
        password = waitElement.get_attribute("value")
        return password

    def warrningBoarderLoginField(self):
        driver = self.app.driver
        border = driver.find_element_by_name("login").value_of_css_property("border-bottom-color")
        return border

    def waitForElementXpath(self, xpathElement):
        waitElement = WebDriverWait(self.app.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, xpathElement)))
        return waitElement

    def waitForElementName(self, nameElement):
        waitElement = WebDriverWait(self.app.driver, 5).until(
            EC.visibility_of_element_located((By.NAME, nameElement)))
        return waitElement