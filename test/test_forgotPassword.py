from random import randrange
random = randrange(100000000)
import time


def test_validEmail(app):
    app.pages.openForgotPasswordPage()
    app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8@gmail.com")
    app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    time.sleep(0.1)
    app.session.currentUrl("/confirmation/")
    assert app.warning.getOuterText("//h2[@class='main_title']") == "Пожалуйста, проверьте Ваш e-mail ящик"

def test_emptyEmail(app):
    app.pages.openForgotPasswordPage()
    app.driver.find_element_by_xpath("//input[@id='email']").send_keys("")
    app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    assert app.warning.getOuterText("//div[@id='reminder-form']/div/span[@class='error_message']") == "E-mail не существует или не подтвержден"
    assert app.warning.getBorderColor("//input[@id='email']") == "rgba(187, 37, 37, 1)"

def test_emptyCaptcha(app):
    app.pages.openForgotPasswordPage()
    app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8@gmail.com")
    app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("")
    app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    assert app.warning.getOuterText("//fieldset[@id='remind_capcha_submit']//span[@class='error_message']") == "Введено неверное значение"
    assert app.warning.getBorderColor("//input[@id='captcha']") == "rgba(187, 37, 37, 1)"

def test_wrongCaptcha(app):
    random = randrange(9999)
    app.pages.openForgotPasswordPage()
    app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8@gmail.com")
    app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys(random)
    app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    assert app.warning.getOuterText("//fieldset[@id='remind_capcha_submit']//span[@class='error_message']") == "Введено неверное значение"
    assert app.warning.getBorderColor("//input[@id='captcha']") == "rgba(187, 37, 37, 1)"

""" Not implemented yet!!!!!!!!

def test_emailNotexist(app):
    app.pages.openForgotPasswordPage()
    app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8" + random + "@gmail.com")
    app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    assert app.warning.getOuterText("//div[@class='password_reminder_fields']/span[2]") == "E-mail не существует или не подтвержден"
    assert app.warning.getBorderColor("//input[@id='captcha']") == "rgba(187, 37, 37, 1)"
"""

def test_emailWithotAt(app):
    app.pages.openForgotPasswordPage()
    app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8gmail.com")
    app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    assert app.warning.getOuterText("//div[@class='password_reminder_fields']/span[2]") == "E-mail не существует или не подтвержден"
    assert app.warning.getBorderColor("//input[@id='captcha']") == "rgba(187, 37, 37, 1)"

def test_emailWithotDomain(app):
    app.pages.openForgotPasswordPage()
    app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8@.com")
    app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    assert app.warning.getOuterText("//div[@class='password_reminder_fields']/span[2]") == "E-mail не существует или не подтвержден"
    assert app.warning.getBorderColor("//input[@id='captcha']") == "rgba(187, 37, 37, 1)"

def test_emailWithotDotCom(app):
    app.pages.openForgotPasswordPage()
    app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8@gmail")
    app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    assert app.warning.getOuterText("//div[@class='password_reminder_fields']/span[2]") == "E-mail не существует или не подтвержден"
    assert app.warning.getBorderColor("//input[@id='captcha']") == "rgba(187, 37, 37, 1)"


def test_emailWithotEmailName(app):
    app.pages.openForgotPasswordPage()
    app.driver.find_element_by_xpath("//input[@id='email']").send_keys("@gmail.com")
    app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    assert app.warning.getOuterText(
        "//div[@class='password_reminder_fields']/span[2]") == "E-mail не существует или не подтвержден"
    assert app.warning.getBorderColor("//input[@id='captcha']") == "rgba(187, 37, 37, 1)"


def test_emailWithotDot(app):
    app.pages.openForgotPasswordPage()
    app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8@gmailcom")
    app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    assert app.warning.getOuterText(
        "//div[@class='password_reminder_fields']/span[2]") == "E-mail не существует или не подтвержден"
    assert app.warning.getBorderColor("//input[@id='captcha']") == "rgba(187, 37, 37, 1)"

def test_emailWithSpaceBefore(app):
    app.pages.openForgotPasswordPage()
    app.driver.find_element_by_xpath("//input[@id='email']").send_keys(" triced8@gmail.com")
    app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    time.sleep(0.1)
    app.session.currentUrl("/confirmation/")
    assert app.warning.getOuterText("//h2[@class='main_title']") == "Пожалуйста, проверьте Ваш e-mail ящик"

def test_emailWithSpaceAfter(app):
    app.pages.openForgotPasswordPage()
    app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8@gmail.com ")
    app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    time.sleep(0.1)
    app.session.currentUrl("/confirmation/")
    assert app.warning.getOuterText("//h2[@class='main_title']") == "Пожалуйста, проверьте Ваш e-mail ящик"

def test_emailUpper(app):
    app.pages.openForgotPasswordPage()
    app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8@gmail.com").upper()
    app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    time.sleep(0.1)
    app.session.currentUrl("/confirmation/")
    assert app.warning.getOuterText("//h2[@class='main_title']") == "Пожалуйста, проверьте Ваш e-mail ящик"



