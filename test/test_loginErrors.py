import time
from model.credLogin import LoginCred
from random import randrange

random = randrange(100000)


def test_emptyFields(app):
    app.session.login(LoginCred(username="", password=""))
    app.session.captchaEntering()
    assert app.warning.getOuterText(
        "(//input[@name='password'])[2]/following::div[1]") == "Почта или пароль указаны неверно"
    assert app.warning.getBorderColor("//div[@id='login']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    assert app.warning.getBorderColor("//input[@name='login']") == "rgba(187, 37, 37, 1)"
    app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()


def test_emptyUserName(app):
    app.session.login(LoginCred(username="", password="TestTest12"))
    app.session.captchaEntering()
    assert app.warning.getOuterText(
        "(//input[@name='password'])[2]/following::div[1]") == "Почта или пароль указаны неверно"
    assert app.warning.getBorderColor("//div[@id='login']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    assert app.warning.getBorderColor("//input[@name='login']") == "rgba(187, 37, 37, 1)"
    app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()


def test_emptyPassword(app):
    app.session.login(LoginCred(username="triced", password=""))
    app.session.captchaEntering()
    assert app.warning.getOuterText(
        "(//input[@name='password'])[2]/following::div[1]") == "Почта или пароль указаны неверно"
    assert app.warning.getBorderColor("//div[@id='login']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    assert app.warning.getBorderColor("//input[@name='login']") == "rgba(187, 37, 37, 1)"
    app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()


def test_loginNotExistUser(app):
    app.session.login(LoginCred(username="triced" + str(random), password="TestTest12"))
    assert app.warning.getOuterText(
        "(//input[@name='password'])[2]/following::div[1]") == "Почта или пароль указаны неверно"
    assert app.warning.getBorderColor("//div[@id='login']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    assert app.warning.getBorderColor("//input[@name='login']") == "rgba(187, 37, 37, 1)"
    app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()


def test_nickNameWithDoteAfter(app1):
    app1.session.login(LoginCred(username="triced.", password="TestTest12"))
    app1.session.captchaEntering()
    assert app1.warning.getOuterText(
        "(//input[@name='password'])[2]/following::div[1]") == "Почта или пароль указаны неверно"
    assert app1.warning.getBorderColor("//div[@id='login']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    assert app1.warning.getBorderColor("//input[@name='login']") == "rgba(187, 37, 37, 1)"
    app1.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()


def test_emailWithDoteAfter(app1):
    app1.session.login(LoginCred(username="triced8+3030@gmail.com.", password="TestTest12"))
    app1.session.captchaEntering()
    assert app1.warning.getOuterText(
        "(//input[@name='password'])[2]/following::div[1]") == "Почта или пароль указаны неверно"
    assert app1.warning.getBorderColor("//div[@id='login']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    assert app1.warning.getBorderColor("//input[@name='login']") == "rgba(187, 37, 37, 1)"
    app1.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()


def test_nickNameWithDoteBefore(app1):
    app1.session.login(LoginCred(username=".triced", password="TestTest12"))
    app1.session.captchaEntering()
    assert app1.warning.getOuterText(
        "(//input[@name='password'])[2]/following::div[1]") == "Почта или пароль указаны неверно"
    assert app1.warning.getBorderColor("//div[@id='login']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    assert app1.warning.getBorderColor("//input[@name='login']") == "rgba(187, 37, 37, 1)"
    app1.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()


def test_loginPasswordCaps(app1):
    app1.session.login(LoginCred(username="triced8+3030@gmail.com", password="TestTest12".upper()))
    app1.session.captchaEntering()
    assert app1.warning.getOuterText(
        "(//input[@name='password'])[2]/following::div[1]") == "Почта или пароль указаны неверно"
    assert app1.warning.getBorderColor("//div[@id='login']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    assert app1.warning.getBorderColor("//input[@name='login']") == "rgba(187, 37, 37, 1)"
    app1.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()
