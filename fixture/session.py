class SessionHelper:

    def __init__(self, app):
        self.app = app

    def opensa(self):
        driver = self.app.driver
        driver.get("https://beta.pokermatch.com/sa")

    def login(self, group):
        driver = self.app.driver
        self.app.openMainPage()
        driver.find_element_by_xpath("//a[2]/span").click()
        driver.find_element_by_name("login").send_keys(group.username)
        driver.find_element_by_xpath("(//input[@name='password'])[2]").send_keys(group.password)
        driver.find_element_by_xpath("//div[@id='login']/div/div/div[2]/form/div[4]/button/div").click()

    def logOut(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//a[@href='/logout/']").click()