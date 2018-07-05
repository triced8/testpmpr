#from model.credLogin import LoginCred
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from fixture.session import SessionHelper

class WarningMessages:

    def __init__(self, app):
        self.app = app

    # Take the warning message by Xpath
    def getOuterText(self, xpath):
        waitElement = self.waitForElementXpath(xpath)
        message = waitElement.get_attribute("outerText")
        return message

    # Take boarder of element by Xpath
    def getBorderColor(self, xpath):
        waitElement = self.waitForElementXpath(xpath)
        border = waitElement.value_of_css_property("border-bottom-color")
        return border

    def passswordFieldGetValue(self, xpath):
        waitElement = self.waitForElementXpath(xpath)
        password = waitElement.get_attribute("value")
        return password


    # Waiting element by Xpath
    def waitForElementXpath(self, xpathElement):
        waitElement = WebDriverWait(self.app.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, xpathElement)))
        return waitElement

    # Waiting element by Name
    def waitForElementName(self, nameElement):
        waitElement = WebDriverWait(self.app.driver, 5).until(
            EC.visibility_of_element_located((By.NAME, nameElement)))
        return waitElement