from selenium import webdriver
from random import randrange
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)

    def openMainPage(self):
        driver = self.driver
        driver.get("https://beta.pokermatch.com/ru")


    def signUp(self):
        driver = self.driver
        self.openMainPage()
        random = randrange(100000)
        driver.find_element_by_xpath("//div[2]/a/span").click()
        driver.find_element_by_name("email").send_keys("triced8+" + str(random) + "@gmail.com")
        driver.find_element_by_name("nick").send_keys("triced" + str(random))
        driver.find_element_by_xpath("(//input[@name='password'])[4]").send_keys("TestTest12")
        driver.find_element_by_xpath("(//input[@name='captcha'])[2]").send_keys("1111")
        driver.find_element_by_xpath("//div[@id='registration']/div/div/div[2]/form/button/div").click()



    def destroy(self):
        self.driver.quit()


