import time



class SignUpHelper:

    def __init__(self, app):
        self.app = app

    def open_signup_popup(self):
        driver = self.app.driver
        #Open main page
        self.app.open_main_page_ru()
        #Open Sign Up pop-up
        driver.find_element_by_xpath("//div[@class='head__inner']/div[2]/a[1]").click()

    def sign_up(self, group):
        driver = self.app.driver
        self.open_signup_popup()
        #Fill in fields
        driver.find_element_by_name("email").send_keys(group.email)
        driver.find_element_by_name("nick").send_keys(group.username)
        driver.find_element_by_xpath("(//input[@name='password'])[4]").send_keys(group.password)
        driver.find_element_by_xpath("(//input[@name='captcha'])[2]").send_keys(group.captcha)
        #Click on the Registration button

        driver.find_element_by_xpath("//div[@id='registration']/div/div/div[2]/form/button/div").click()

    def sign_up_happy_pass(self, group):
        driver = self.app.driver
        self.open_signup_popup()
        #Fill in fields
        driver.find_element_by_name("email").send_keys(group.email)
        driver.find_element_by_name("nick").send_keys(group.username)
        driver.find_element_by_xpath("(//input[@name='password'])[4]").send_keys(group.password)
        driver.find_element_by_xpath("(//input[@name='captcha'])[2]").send_keys(group.captcha)
        assert self.app.warning.get_outer_text("//span[@class='modala__ok']") == "Этот логин доступен"
        assert self.app.warning.get_border_color("//div[@id='registration']//input[@id='login']") == "rgba(0, 128, 0, 1)"
        #Click on the Registration button
        driver.find_element_by_xpath("//div[@id='registration']/div/div/div[2]/form/button/div").click()

    def clear_cache(self):
        driver = self.app.driver
        """Clear the cookies and cache for the ChromeDriver instance."""
        # navigate to the settings page
        driver.get('chrome://settings/clearBrowserData')
        # click the button to clear the cache
        driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm').click()

    def error_sign_up(self):
        driver = self.app.driver
        if driver.current_url.endswith("/later/registration/"):
            self.app.open_main_page_ru()
            print("Yess!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            #driver.get("https://beta.pokermatch.com/ru#registration")
            return True
        else:
            print("NO!!!!!!!!!!!!!!!!!!!!!!!!!!!")



