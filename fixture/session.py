from selenium.common.exceptions import NoSuchElementException
import time

from fixture.warningMessages import WarningMessages
from selenium.webdriver import ActionChains


class SessionHelper:

    def __init__(self, app):
        self.app = app
        self.warning = WarningMessages(self)

    def open_login_popup(self):
        driver = self.app.driver
        # Open main page
        self.app.open_main_page_ru()
        # Open LogIn pop-up
        driver.find_element_by_xpath(self.app.selectors.login_button).click()
        return driver

    def login(self, group):
        driver = self.open_login_popup()
        self.current_url(endswith="#login")
        # Fill in fields
        driver.find_element_by_name(self.app.selectors.login_field).clear()
        driver.find_element_by_name(self.app.selectors.login_field).send_keys(group.username)
        driver.find_element_by_xpath(self.app.selectors.login_password_field).clear()
        driver.find_element_by_xpath(self.app.selectors.login_password_field).send_keys(group.password)
        # Click on the login button
        driver.find_element_by_xpath(self.app.selectors.login_button_form).click()
        #driver.delete_all_cookies()

    def logout(self):
        driver = self.app.driver
        # Click on the logout button
        driver.find_element_by_xpath(self.app.selectors.logout_button).click()

    # Fill fields at the login pop-up
    def fill_fields_see_password(self, group):
        driver = self.open_login_popup()
        self.current_url(endswith="#login")
        # Fill in fields
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys(group.username)
        driver.find_element_by_xpath("(//input[@name='password'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='password'])[2]").send_keys(group.password)
        driver.find_element_by_xpath("//div[@id='login']//span[@class='switch_pass']").click()

    # Compare user nickname with logged nickname
    def is_logged_as(self, username):
        driver = self.app.driver
        return driver.find_element_by_xpath("//div[@class='info-list__item info-list__item_type_nick']//a").text == username

    # Check that page have logout button
    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements_by_xpath("//a[@href='/logout/']")) > 0

    # If nickname is different logout and login
    def ensure_login(self, username):
        if self.is_logged_in():
            if self.is_logged_as(username):
                return
            else:
                self.logout()
        self.login(username)

    # Take xpath of the logout button
    def user_logged(self):
        xpath = "//a[@href='/logout/']"
        return self.check_exists_by_xpath(xpath)


    # Check that element is Exists on the page

    def check_exists_by_xpath(self, xpath):
        driver = self.app.driver
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def current_url(self, endswith):
        driver = self.app.driver
        assert driver.current_url.endswith(endswith)

    """
    def ensureLogout(self):
        driver = self.app.driver
        if len(driver.find_element_by_xpath("//a[@href='/logout/']")) >0:
            self.logout()
        else:
            self.app.openMainPage()
            self.logout()
    """

    # Enter Captcha if is enable
    def captcha_entering(self):
        xpath = "//div[@id='login']/div[@role='document']//form[@action='/login/']//input[@name='captcha']"
        driver = self.app.driver
        element = driver.find_element_by_xpath(xpath)
        time.sleep(0.1)
        if self.element_is_display(xpath):
            element.send_keys("1111")
            driver.find_element_by_xpath("//form[@action='/login/']//div[@class='modala-button__text']").click()

    # Click outside the login pop-up
    def click_out_side(self):
        driver = self.app.driver
        action = ActionChains(driver)
        action.move_by_offset(5, 5).click()
        action.perform()

    def element_is_display(self, xpath):
        driver = self.app.driver
        element = driver.find_element_by_xpath(xpath)
        return element.is_displayed()