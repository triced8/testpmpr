
class SignUpHelper:

    def __init__(self, app):
        self.app = app


    def signUp(self, group):
        driver = self.app.driver
        #Open main page
        self.app.openMainPage()
        #Open Sign Up pop-up
        driver.find_element_by_xpath("//div[@class='head__inner']/div[2]/a[1]").click()
        #Fill in fields
        driver.find_element_by_name("email").send_keys(group.email)
        driver.find_element_by_name("nick").send_keys(group.username)
        driver.find_element_by_xpath("(//input[@name='password'])[4]").send_keys(group.password)
        driver.find_element_by_xpath("(//input[@name='captcha'])[2]").send_keys(group.captcha)
        #Click on the Registration button
        driver.find_element_by_xpath("//div[@id='registration']/div/div/div[2]/form/button/div").click()
