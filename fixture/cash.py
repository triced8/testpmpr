from selenium.webdriver import ActionChains
import time
from fixture import selectors
from fixture.session import SessionHelper

"""
Number: 4000 0000 0000 0002
Valid: 12/2020
Holder: Dmitry
CVV: 111
"""

cash_button_list = selectors.Selectors.cash_button_ua_list
cash_field = selectors.Selectors.cash_field_list


class Cash:

    def __init__(self, app):
        self.app = app

    def open_inner_frame(self):
        driver = self.app.driver
        for i in cash_button_list:
            driver.find_element_by_xpath(i).click()
            for j in cash_field:
                self.app.session.element_is_display(j)



"""
    def fill_card_form(self):
        driver = self.app.driver
        amount = "200"
        # The card's number is incorrect entered to field so "2" should be after "4" to entered as last
        driver.find_element_by_xpath("//input[@name='card_number']").send_keys("4200000000000000")
        # element to scroll
        melement = driver.find_element_by_xpath("//div[@class='mCSB_container']/div[@value='4']")
        # element which scroll
        # screlement = driver.find_element_by_xpath("//*[@id='mCSB_2']/div[2]/div/div[1]/div")
        # ActionChains(driver).drag_and_drop(screlement, melement).perform()
        # choose month
        # driver.find_element_by_xpath("//div[@id='valid_thru_month']//div[@class='sel_arraw']").click()  # arrow of month list
        # ActionChains(driver).drag_and_drop(screlement, melement).perform()
        time.sleep(0.5)
        melement.click()
        # choose year
        driver.find_element_by_xpath(
            "//div[@id='valid_thru_year']//div[@class='sel_arraw']").click()  # arrow of year list
        driver.find_element_by_xpath("//div[@class='mCSB_container']//div[@value='2020']").click()
        time.sleep(0.5)
        # enter cvv
        driver.find_element_by_xpath("//input[@id='cvv']").send_keys("111")
        # enter card holder
        driver.find_element_by_xpath("//input[@id='card_holder']").send_keys("Dmitry")
        # enter amount
        driver.find_element_by_xpath("//input[@id='amount_input']").clear()
        driver.find_element_by_xpath("//input[@id='amount_input']").send_keys(amount)
        # submit cash-in
        driver.find_element_by_xpath("//button[@id='submit_button']").click()
        self.app.warning.wait_for_element_xpath("//div[@class='payment_message success']")
        assert self.app.warning.get_outer_text(
            "//div[@class='payment_details no_voucher']//p[2]") == "Сумма: " + amount + " UAH"
"""
