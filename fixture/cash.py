from selenium.webdriver import ActionChains
import time
from fixture import selectors


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

    def open_inner_frames(self):
        driver = self.app.driver
        for i in cash_button_list:
            driver.find_element_by_xpath(i).click()
            for j in cash_field:
                self.app.session.element_is_display(j)


    def open_inner_frame(self, xpath_cash, xpath):
        driver = self.app.driver
        driver.find_element_by_xpath(xpath_cash).click()
        self.app.session.element_is_display(xpath)

    def fill_inner_frame(self, xpath):
        driver = self.app.driver
        time.sleep(1)
        driver.find_element_by_xpath(xpath).send_keys("400")
        driver.find_element_by_xpath("//div[@class='pm_cash__table pm_cash__table_in']/div[3]//form[@class='pm_cash__left']//span[@class='button__inner']").click()

    def fill_ecommpay_fields(self):
        driver = self.app.driver
        self.app.warning.wait_for_element_xpath(self.app.selectors.ecommpay_inner_cash_button)
        driver.find_element_by_xpath(self.app.selectors.ecommpay_inner_cash_button).click()
        self.app.pages.frame_switch("//div[@class='pm_cash__table pm_cash__table_in']/div[5]//iframe")
        self.app.warning.wait_for_element_xpath("//input[@class='card_number'][1]")
        driver.find_element_by_xpath("//input[@class='card_number'][1]").send_keys("4020000000000000")
        driver.find_element_by_xpath("//input[@name='exp_month']").send_keys("11")
        driver.find_element_by_xpath("//input[@id='year']").send_keys("23")
        driver.find_element_by_xpath("//input[@name='holder']").send_keys("ABD CDE")
        driver.find_element_by_xpath("//input[@name='cvv']").send_keys("321")
        driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(3)

    def open_privat_inner_frame(self):
        buttons_list = self.get_list_of_dep_button()
        buttons_list[4].click()

    def open_privat_page(self):
        driver = self.app.driver
        driver.execute_script("window.scrollTo(0, 300);")
        buttons_list = self.get_list_of_dep_button()
        time.sleep(0.5)
        buttons_list[5].click()
        time.sleep(7)


    def open_web_money_inner_frame(self):
        driver = self.app.driver
        driver.execute_script("window.scrollTo(0, 500);")
        buttons_list = self.get_list_of_dep_button()
        buttons_list[6].click()

    def open_web_money_frame(self):
        driver = self.app.driver
        buttons_list = self.get_list_of_dep_button()
        buttons_list[7].click()
        self.app.pages.frame_switch("//div[@class='pm_cash__content'][4]//iframe")
        time.sleep(5)



    def open_qiwi_inner_frame(self):
        driver = self.app.driver
        driver.execute_script("window.scrollTo(0, 500);")
        buttons_list = self.get_list_of_dep_button()
        buttons_list[8].click()

    def open_qiwi_frame(self):
        driver = self.app.driver
        buttons_list = self.get_list_of_dep_button()
        buttons_list[9].click()
        self.app.pages.frame_switch("//div[@class='pm_cash__content'][5]//iframe")
        time.sleep(7)

    def open_skrill_inner_frame(self):
        driver = self.app.driver
        driver.execute_script("window.scrollTo(0, 500);")
        buttons_list = self.get_list_of_dep_button()
        buttons_list[10].click()

    def open_skrill_frame(self):
        driver = self.app.driver
        buttons_list = self.get_list_of_dep_button()
        buttons_list[11].click()
        time.sleep(5)
        self.app.pages.frame_switch("//div[@class='pm_cash__content'][6]//iframe")

    def open_neteller_inner_frame(self):
        driver = self.app.driver
        driver.execute_script("window.scrollTo(0, 500);")
        buttons_list = self.get_list_of_dep_button()
        buttons_list[12].click()

    def open_neteller_frame(self):
        driver = self.app.driver
        buttons_list = self.get_list_of_dep_button()
        buttons_list[13].click()
        time.sleep(5)
        self.app.pages.frame_switch("//div[@class='pm_cash__content'][7]//iframe")

    def open_yad_inner_frame(self):
        driver = self.app.driver
        driver.execute_script("window.scrollTo(0, 600);")
        buttons_list = self.get_list_of_dep_button()
        buttons_list[14].click()

    def open_yad_page(self):
        driver = self.app.driver
        driver.execute_script("window.scrollTo(0, 600);")
        buttons_list = self.get_list_of_dep_button()
        time.sleep(0.5)
        buttons_list[15].click()
        time.sleep(1)
        self.app.pages.switch_to_new_tab()

    def open_adv_inner_frame(self):
        driver = self.app.driver
        buttons_list = self.get_list_of_dep_button()
        driver.execute_script("window.scrollTo(0, 600);")
        buttons_list[16].click()

    def open_adv_page(self):
        driver = self.app.driver
        buttons_list = self.get_list_of_dep_button()
        time.sleep(0.5)
        buttons_list[17].click()
        time.sleep(5)
        self.app.pages.switch_to_new_tab()

    def open_kiev_star_page(self):
        driver = self.app.driver
        driver.execute_script("window.scrollTo(0, 600);")
        driver.find_element_by_xpath("//a[@href='https://money.kyivstar.ua/ru/service/view/pokermatch']").click()
        time.sleep(5)
        self.app.pages.switch_to_new_tab()

    def open_life_page(self):
        driver = self.app.driver
        driver.execute_script("window.scrollTo(0, 600);")
        driver.find_element_by_xpath("//a[@href='https://paycell.lifecell.ua/category-onlinetopup/pk-match']").click()
        time.sleep(5)
        self.app.pages.switch_to_new_tab()

    def get_list_of_dep_button(self):
        driver = self.app.driver
        dep_buttons_dep = driver.find_elements_by_xpath("//div[@class='pm_cash__table pm_cash__table_in']//button[child::span[@class='button__inner']]")
        dep_list = []
        for button in dep_buttons_dep:
            dep_list.append(button)
        return dep_list







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
