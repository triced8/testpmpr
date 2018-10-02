from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WarningMessages:

    def __init__(self, app):
        self.app = app

    # Take the warning message by Xpath
    def get_outer_text(self, xpath):
        waitElement = self.wait_for_element_xpath(xpath)
        message = waitElement.get_attribute("outerText")
        return message

    # Take boarder of element by Xpath
    def get_border_color(self, xpath):
        waitElement = self.wait_for_element_xpath(xpath)
        border = waitElement.value_of_css_property("border-bottom-color")
        return border

    def get_value(self, xpath):
        waitElement = self.wait_for_element_xpath(xpath)
        password = waitElement.get_attribute("value")
        return password

    # Waiting element by Xpath
    def wait_for_element_xpath(self, xpathElement):
        waitElement = WebDriverWait(self.app.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, xpathElement)))
        return waitElement

    # Waiting element by Name
    def wait_for_element_name(self, nameElement):
        waitElement = WebDriverWait(self.app.driver, 5).until(
            EC.visibility_of_element_located((By.NAME, nameElement)))
        return waitElement


