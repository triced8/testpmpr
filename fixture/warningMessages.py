#from model.credLogin import LoginCred
import time


class WarningMessages:

    def __init__(self, app):
        self.app = app

    def warrningMessageFromLoginPopUp(self):
        driver = self.app.driver
        message = driver.find_element_by_xpath("(//input[@name='password'])[2]/following::div[1]").get_attribute("outerText")
        return message

    def warrningBoarderPasswordField(self):
        driver = self.app.driver
        border = driver.find_element_by_name("password").value_of_css_property("border-bottom-color")
        return border