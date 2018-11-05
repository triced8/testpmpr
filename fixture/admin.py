from model.credLogin import LoginCred
import time

class AdminHelper:

    def __init__(self, app):
        self.app = app

    def open_admin(self):
        driver = self.app.driver
        driver.get(self.app.selectors.site_admin)

    def login_as_admin(self):
        self.app.pages.open_main_page()
        self.app.session.login(LoginCred(username="tricedu", password="TestTest12"))
        self.open_admin()

    def open_first_user(self):
        driver = self.app.driver
        self.login_as_admin()
        self.app.warning.wait_for_element_xpath(self.app.selectors.user_button)
        driver.find_element_by_xpath(self.app.selectors.user_button).click()
        driver.find_element_by_xpath(self.app.selectors.first_user).click()

    def open_email_page(self):
        driver = self.app.driver
        self.open_first_user()
        driver.find_element_by_xpath(self.app.selectors.email_header_link).click()

    def open_registration_email(self):
        driver = self.app.driver
        self.open_email_page()
        driver.find_element_by_xpath(self.app.selectors.registration_email).click()

    def click_to_registration_link(self):
        driver = self.app.driver
        self.open_registration_email()
        driver.find_element_by_xpath(self.app.selectors.registration_link).click()

    def registration_with_approve(self):
        driver = self.app.driver
        self.app.pages.open_main_page()
        self.app.session.login(LoginCred(username="tricedu", password="TestTest12"))
        driver.refresh()
        driver.get(self.app.selectors.site_admin)
        self.app.warning.wait_for_element_xpath(self.app.selectors.user_button)
        driver.find_element_by_xpath(self.app.selectors.user_button).click()
        driver.find_element_by_xpath(self.app.selectors.first_user).click()
        driver.find_element_by_xpath(self.app.selectors.email_header_link).click()
        driver.find_element_by_xpath(self.app.selectors.registration_email).click()
        window_after = driver.window_handles[1]
        driver.switch_to_window(window_after)
        driver.find_element_by_xpath(self.app.selectors.registration_link).click()
        time.sleep(3)