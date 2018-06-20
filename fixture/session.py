

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, group):
        driver = self.app.driver
        self.app.openMainPage()
        driver.find_element_by_xpath("//a[2]/span").click()
        driver.find_element_by_name("login").send_keys(group.username)
        driver.find_element_by_xpath("(//input[@name='password'])[2]").send_keys(group.password)
        driver.find_element_by_xpath("//div[@id='login']/div/div/div[2]/form/div[4]/button/div").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[@href='/logout/']").click()

    def isLoggedAs(self, username):
        driver = self.app.driver
        return driver.find_element_by_xpath("//a[@href='https://beta.pokermatch.com/ru/page/account']").text == username

    def isLoggedIn(self):
        driver = self.app.driver
        return len(driver.find_elements_by_xpath("//a[@href='/logout/']")) > 0

    def ensureLogin(self, username, password):
        driver = self.app.driver
        if self.isLoggedIn():
            if self.isLoggedAs(username):
                return
            else:
                self.logout()
        self.login(username, password)
"""
    def ensureLogout(self):
        driver = self.app.driver
        if len(driver.find_element_by_xpath("//a[@href='/logout/']")) >0:
            self.logout()
        else:
            self.app.openMainPage()
            self.logout()
"""