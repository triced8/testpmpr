from random import randrange
random = randrange(100000000)
import time
import pytest

@pytest.allure.step("Forgot password with valid Email")
def test_validEmail(app):
    with pytest.allure.step("Open Forgot Password page"):
        app.pages.openForgotPasswordPage()
    with pytest.allure.step("Enter Email in to the 'email' field"):
        app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8+3232@gmail.com")
    with pytest.allure.step("Enter Email in to the 'captcha' field"):
        app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    with pytest.allure.step("Click on the 'Send' button"):
        app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    time.sleep(1)
    with pytest.allure.step("Check current URL after sending email"):
        app.session.currentUrl("/mailed/")
    with pytest.allure.step("Check text after sending email"):
        assert app.warning.getOuterText("//h2[@class='main_title']") == "Мы отправили Вам ссылку для авторизации. Вы сможете сменить пароль в настройках профиля"

@pytest.allure.step("Forgot password With Space before Email")
def test_emailWithSpaceBefore(app):
    with pytest.allure.step("Open Forgot Password page"):
        app.pages.openForgotPasswordPage()
    with pytest.allure.step("Enter Space before Email"):
        app.driver.find_element_by_xpath("//input[@id='email']").send_keys(" triced8@gmail.com")
    with pytest.allure.step("Enter Email in to the 'captcha' field"):
        app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    with pytest.allure.step("Click on the 'Send' button"):
        app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    time.sleep(0.1)
    with pytest.allure.step("Check current URL after sending email"):
        app.session.currentUrl("/confirmation/")
    with pytest.allure.step("Check warning message"):
        assert app.warning.getOuterText("//h2[@class='main_title']") == "Пожалуйста, проверьте Ваш e-mail ящик"

@pytest.allure.step("Forgot password With space after Email")
def test_emailWithSpaceAfter(app):
    with pytest.allure.step("Open Forgot Password page"):
        app.pages.openForgotPasswordPage()
    with pytest.allure.step("Enter Space after Email"):
        app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8@gmail.com ")
    with pytest.allure.step("Enter Email in to the 'captcha' field"):
        app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    with pytest.allure.step("Click on the 'Send' button"):
        app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    time.sleep(0.1)
    with pytest.allure.step("Check current URL after sending email"):
        app.session.currentUrl("/confirmation/")
    with pytest.allure.step("Check warning message"):
        assert app.warning.getOuterText("//h2[@class='main_title']") == "Пожалуйста, проверьте Ваш e-mail ящик"

@pytest.allure.step("Forgot password With UpperCase Email")
def test_emailUpper(app):
    with pytest.allure.step("Open Forgot Password page"):
        app.pages.openForgotPasswordPage()
    with pytest.allure.step("Enter Email with uppercase"):
        app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8@gmail.com").upper()
    with pytest.allure.step("Enter Email in to the 'captcha' field"):
        app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    with pytest.allure.step("Click on the 'Send' button"):
        app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    time.sleep(0.1)
    with pytest.allure.step("Check current URL after sending email"):
        app.session.currentUrl("/confirmation/")
    with pytest.allure.step("Check warning message"):
        assert app.warning.getOuterText("//h2[@class='main_title']") == "Пожалуйста, проверьте Ваш e-mail ящик"

@pytest.allure.step("Forgot password with empty Email")
def test_emptyEmail(app):
    with pytest.allure.step("Open Forgot Password page"):
        app.pages.openForgotPasswordPage()
    with pytest.allure.step("Enter Empty Email in to the 'email' field"):
        app.driver.find_element_by_xpath("//input[@id='email']").send_keys("")
    with pytest.allure.step("Enter Email in to the 'captcha' field"):
        app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    with pytest.allure.step("Click on the 'Send' button"):
        app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    with pytest.allure.step("Check warning message"):
        assert app.warning.getOuterText("//div[@id='reminder-form']/div/span[@class='error_message']") == "E-mail не существует или не подтвержден"
    with pytest.allure.step("Check warning boarder at the 'email' field"):
        assert app.warning.getBorderColor("//input[@id='email']") == "rgba(187, 37, 37, 1)"

@pytest.allure.step("Forgot password with empty captcha")
def test_emptyCaptcha(app):
    with pytest.allure.step("Open Forgot Password page"):
        app.pages.openForgotPasswordPage()
    with pytest.allure.step("Enter Email in to the 'email' field"):
        app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8@gmail.com")
    with pytest.allure.step("Enter Empty captcha"):
        app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("")
    with pytest.allure.step("Click on the 'Send' button"):
        app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    with pytest.allure.step("Check warning message"):
        assert app.warning.getOuterText("//fieldset[@id='remind_capcha_submit']//span[@class='error_message']") == "Введено неверное значение"
    with pytest.allure.step("Check warning boarder at the 'captcha' field"):
        assert app.warning.getBorderColor("//input[@id='captcha']") == "rgba(187, 37, 37, 1)"

@pytest.allure.step("Forgot password with wrong captcha")
def test_wrongCaptcha(app):
    random = randrange(9999)
    with pytest.allure.step("Open Forgot Password page"):
        app.pages.openForgotPasswordPage()
    with pytest.allure.step("Enter Email in to the 'email' field"):
        app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8@gmail.com")
    with pytest.allure.step("Enter wrong captcha"):
        app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys(random)
    with pytest.allure.step("Click on the 'Send' button"):
        app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    with pytest.allure.step("Check warning message"):
        assert app.warning.getOuterText("//fieldset[@id='remind_capcha_submit']//span[@class='error_message']") == "Введено неверное значение"
    with pytest.allure.step("Check warning boarder at the 'captcha' field"):
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

@pytest.allure.step("Forgot password without AT Email")
def test_emailWithotAt(app):
    with pytest.allure.step("Open Forgot Password page"):
        app.pages.openForgotPasswordPage()
    with pytest.allure.step("Enter wrong Email without AT"):
        app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8gmail.com")
    with pytest.allure.step("Enter Email in to the 'captcha' field"):
        app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    with pytest.allure.step("Click on the 'Send' button"):
        app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    with pytest.allure.step("Check warning message"):
        assert app.warning.getOuterText("//div[@class='password_reminder_fields']/span[2]") == "E-mail не существует или не подтвержден"
    with pytest.allure.step("Check warning boarder at the 'email' field"):
        assert app.warning.getBorderColor("//input[@id='email']") == "rgba(187, 37, 37, 1)"

@pytest.allure.step("Forgot password Withot Domain")
def test_emailWithotDomain(app):
    with pytest.allure.step("Open Forgot Password page"):
        app.pages.openForgotPasswordPage()
    with pytest.allure.step("Enter wrong Email without Domain"):
        app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8@.com")
    with pytest.allure.step("Enter Email in to the 'captcha' field"):
        app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    with pytest.allure.step("Click on the 'Send' button"):
        app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    with pytest.allure.step("Check warning message"):
        assert app.warning.getOuterText("//div[@class='password_reminder_fields']/span[2]") == "E-mail не существует или не подтвержден"
    with pytest.allure.step("Check warning boarder at the 'email' field"):
        assert app.warning.getBorderColor("//input[@id='email']") == "rgba(187, 37, 37, 1)"

@pytest.allure.step("Forgot password Withot Dot com")
def test_emailWithotDotCom(app):
    with pytest.allure.step("Open Forgot Password page"):
        app.pages.openForgotPasswordPage()
    with pytest.allure.step("Enter wrong Email without Dot com"):
        app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8@gmail")
    with pytest.allure.step("Enter Email in to the 'captcha' field"):
        app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    with pytest.allure.step("Click on the 'Send' button"):
        app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    with pytest.allure.step("Check warning message"):
        assert app.warning.getOuterText("//div[@class='password_reminder_fields']/span[2]") == "E-mail не существует или не подтвержден"
    with pytest.allure.step("Check warning boarder at the 'email' field"):
        assert app.warning.getBorderColor("//input[@id='captcha']") == "rgba(187, 37, 37, 1)"

@pytest.allure.step("Forgot password Withot Email name")
def test_emailWithotEmailName(app):
    with pytest.allure.step("Open Forgot Password page"):
        app.pages.openForgotPasswordPage()
    with pytest.allure.step("Enter wrong Email without Email name"):
        app.driver.find_element_by_xpath("//input[@id='email']").send_keys("@gmail.com")
    with pytest.allure.step("Enter Email in to the 'captcha' field"):
        app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    with pytest.allure.step("Click on the 'Send' button"):
        app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    with pytest.allure.step("Check warning message"):
        assert app.warning.getOuterText(
        "//div[@class='password_reminder_fields']/span[2]") == "E-mail не существует или не подтвержден"
    with pytest.allure.step("Check warning boarder at the 'email' field"):
        assert app.warning.getBorderColor("//input[@id='captcha']") == "rgba(187, 37, 37, 1)"

@pytest.allure.step("Forgot password Withot Dot")
def test_emailWithotDot(app):
    with pytest.allure.step("Open Forgot Password page"):
        app.pages.openForgotPasswordPage()
    with pytest.allure.step("Enter wrong Email without Dot"):
        app.driver.find_element_by_xpath("//input[@id='email']").send_keys("triced8@gmailcom")
    with pytest.allure.step("Enter Email in to the 'captcha' field"):
        app.driver.find_element_by_xpath("//input[@id='captcha']").send_keys("1111")
    with pytest.allure.step("Click on the 'Send' button"):
        app.driver.find_element_by_xpath("//button[@id='passwordreminder']").click()
    with pytest.allure.step("Check warning message"):
        assert app.warning.getOuterText(
        "//div[@class='password_reminder_fields']/span[2]") == "E-mail не существует или не подтвержден"
    with pytest.allure.step("Check warning boarder at the 'email' field"):
        assert app.warning.getBorderColor("//input[@id='captcha']") == "rgba(187, 37, 37, 1)"






