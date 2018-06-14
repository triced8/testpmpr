import unittest
from random import randrange

from selenium import webdriver
from .credLogin import Group

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://pokermatch.com/ru"
        self.verificationErrors = []
        self.accept_next_alert = True

    def openMainPage(self, driver):
        driver.get("https://pokermatch.com/ru")

    def login(self, driver, group):
        driver.find_element_by_xpath("//a[2]/span").click()
        driver.find_element_by_name("login").send_keys(group.username)
        driver.find_element_by_xpath("(//input[@name='password'])[2]").send_keys(group.password)
        driver.find_element_by_xpath("//div[@id='login']/div/div/div[2]/form/div[4]/button/div").click()

    def ssignUp(self, driver):
        random = randrange(100000)
        driver.get("https://beta.pokermatch.com/ru#")
        driver.find_element_by_xpath("//div[2]/a/span").click()
        driver.find_element_by_name("email").send_keys("triced8+" + str(random) + "@gmail.com")
        driver.find_element_by_name("nick").send_keys("triced" + str(random))
        driver.find_element_by_xpath("(//input[@name='password'])[4]").send_keys("TestTest12")
        driver.find_element_by_xpath("(//input[@name='captcha'])[2]").send_keys("1111")
        driver.find_element_by_xpath("//div[@id='registration']/div/div/div[2]/form/button/div").click()

    def test_login(self):
        driver = self.driver
        self.openMainPage(driver)
        self.login(driver, Group(username="triced", password="TestTest12"))

    def test_signUp(self):
        driver = self.driver
        self.openMainPage(driver)
        self.ssignUp(driver)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
