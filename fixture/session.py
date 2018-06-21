from selenium.common.exceptions import NoSuchElementException


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, group):
        driver = self.app.driver
        # Open main page
        self.app.openMainPageRu()
        # Open LogIn pop-up
        driver.find_element_by_xpath("//a[2]/span").click()
        # Fill in fields
        driver.find_element_by_name("login").send_keys(group.username)
        driver.find_element_by_xpath("(//input[@name='password'])[2]").send_keys(group.password)
        # Click on the login button
        driver.find_element_by_xpath("//div[@id='login']/div/div/div[2]/form/div[4]/button/div").click()

    def logout(self):
        driver = self.app.driver
        # Click on the logout button
        driver.find_element_by_xpath("//a[@href='/logout/']").click()

    # Compare user nickname with logged nickname
    def isLoggedAs(self,  username):
        driver = self.app.driver
        return driver.find_element_by_xpath("//a[@href='https://beta.pokermatch.com/ru/page/account']").text == username

    # Check that page have logout button
    def isLoggedIn(self):
        driver = self.app.driver
        return len(driver.find_elements_by_xpath("//a[@href='/logout/']")) > 0

    # If nickname is different logout and login
    def ensureLogin(self, username, password):
        driver = self.app.driver
        if self.isLoggedIn():
            if self.isLoggedAs(username):
                return
            else:
                self.logout()
        self.login(username, password)

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
            return False
        return True


"""
    def ensureLogout(self):
        driver = self.app.driver
        if len(driver.find_element_by_xpath("//a[@href='/logout/']")) >0:
            self.logout()
        else:
            self.app.openMainPage()
            self.logout()
"""
