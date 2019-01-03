from model.credLogin import LoginCred
import time

class AdminHelper:

    def __init__(self, app):
        self.app = app

    def open_admin(self):
        driver = self.app.driver
        driver.get(self.app.selectors.site_admin)

    """





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
"""


    def open_user_registration_email(self):
        driver = self.app.driver
        driver.find_element_by_xpath(self.app.selectors.user_button).click()
        driver.find_element_by_xpath(self.app.selectors.first_user).click()  # Open first user
        driver.find_element_by_xpath(self.app.selectors.email_header_link).click()  # Open email/sms tab
        driver.find_element_by_xpath(self.app.selectors.registration_email).click()  # Open registration email

    def login_as_admin(self):
        driver = self.app.driver
        self.app.pages.open_main_page()
        self.app.session.login(LoginCred(username="tricedu", password="TestTest12"))
        driver.refresh()
        driver.get(self.app.selectors.site_admin)
        self.app.warning.wait_for_element_xpath(self.app.selectors.user_button)

    def registration_with_approve(self):
        driver = self.app.driver
        self.login_as_admin()
        self.open_user_registration_email()
        self.app.pages.switch_to_new_tab()
        driver.find_element_by_xpath(self.app.selectors.registration_link).click()  # Click to registration link

    def get_users_id(self):
        driver = self.app.driver
        ids = driver.find_elements_by_xpath("//td[@name='uid']")
        for id in ids:
            id2 = id.get_attribute("outerText")
            print(id2)
        print(len(ids))

    def open_users_page(self):
        driver = self.app.driver
        driver.get("https://beta.pokermatch.com/sa/users/all/")

    def get_user_for_month(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//button[@value='month']").click()

