from selenium.common.exceptions import NoSuchElementException
import time
from fixture.warningMessages import WarningMessages
from selenium.webdriver import ActionChains


class SessionHelper:

    def __init__(self, app):
        self.app = app
        self.warning = WarningMessages(self)


    def openLoginPopup(self):
        driver = self.app.driver
        # Open main page
        self.app.openMainPageRu()
        # Open LogIn pop-up
        driver.find_element_by_xpath("//a[2]/span").click()
        return driver

    def login(self, group):
        driver = self.openLoginPopup()
        self.currentUrl(endswith="#login")
        # Fill in fields
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys(group.username)
        driver.find_element_by_xpath("(//input[@name='password'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='password'])[2]").send_keys(group.password)
        # Click on the login button
        driver.find_element_by_xpath("//form[@action='/login/']//div[@class='modala-button__text']").click()
        #driver.delete_all_cookies()


    def logout(self):
        driver = self.app.driver
        # Click on the logout button
        driver.find_element_by_xpath("//a[@href='/logout/']").click()

    # Fill fields at the login pop-up
    def fillFieldsSeePasword(self, group):
        driver = self.openLoginPopup()
        self.currentUrl(endswith="#login")
        # Fill in fields
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys(group.username)
        driver.find_element_by_xpath("(//input[@name='password'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='password'])[2]").send_keys(group.password)
        driver.find_element_by_xpath("//div[@id='login']//span[@class='switch_pass']").click()

    # Compare user nickname with logged nickname
    def isLoggedAs(self,  username):
        driver = self.app.driver
        return driver.find_element_by_xpath("//a[@href='https://beta.pokermatch.com/ru/page/account']").text == username

    # Check that page have logout button
    def isLoggedIn(self):
        driver = self.app.driver
        return len(driver.find_elements_by_xpath("//a[@href='/logout/']")) > 0

    # If nickname is different logout and login
    def ensureLogin(self, username):
        if self.isLoggedIn():
            if self.isLoggedAs(username):
                return
            else:
                self.logout()
        self.login(username)

    # Take xpath of the logout button
    def userLogged(self):
        xpath = "//a[@href='/logout/']"
        return self.checkExistsByXpath(xpath)


    # Check that element is Exists on the page
    def checkExistsByXpath(self, xpath):
        driver = self.app.driver
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False and print ("No!!!")
        return True and print ("Yes!!!")

    def currentUrl(self, endswith):
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
    def elementIsDisplay(self, xpath):
        driver = self.app.driver
        element = driver.find_element_by_xpath(xpath)
        return element.is_displayed()

    # Enter Captcha if is enable
    def captchaEntering(self):
        xpath = "//div[@id='login']/div[@role='document']//form[@action='/login/']//input[@name='captcha']"
        driver = self.app.driver
        element = driver.find_element_by_xpath(xpath)
        time.sleep(0.1)
        if self.elementIsDisplay(xpath):
            element.send_keys("1111")
            driver.find_element_by_xpath("//form[@action='/login/']//div[@class='modala-button__text']").click()

    # Click outside the login pop-up
    def clickOutSide(self):
        driver = self.app.driver
        action = ActionChains(driver)
        action.move_by_offset(5, 5).click()
        action.perform()

