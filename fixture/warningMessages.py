#from model.credLogin import LoginCred
import time
#from fixture.application import Application
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WarningMessages:

    def __init__(self, app):
        self.app = app
        #self.gg = Application

    def warrningMessageFromLoginPopUp(self):
        driver = self.app.driver
        waitElement = self.waitForElement("(//input[@name='password'])[2]/following::div[1]")
        message = waitElement.get_attribute("outerText")
        return message

    def waitForElement(self, xpathElement):
        waitElement = WebDriverWait(self.app.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, xpathElement)))
        return waitElement

    def warrningBoarderPasswordField(self):
        driver = self.app.driver
        border = driver.find_element_by_name("password").value_of_css_property("border-bottom-color")
        return border


    def warrningBoarderLoginField(self):
        driver = self.app.driver
        name = "login"
    #    self.gg.wait(name)
        border = driver.find_element_by_name(name).value_of_css_property("border-bottom-color")
        return border
