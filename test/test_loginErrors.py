import time
from model.credLogin import LoginCred
from random import randrange

random = randrange(100000)

def test_emptyFields(app):
    app.session.login(LoginCred(username="", password=""))
    app.session.captchaEntering()
    assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
    assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"
    assert app.warning.warrningBoarderLoginField() == "rgba(187, 37, 37, 1)"
    app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()

def test_emptyUserName(app):
    app.session.login(LoginCred(username="", password="TestTest12"))
    app.session.captchaEntering()
    assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
    assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"
    assert app.warning.warrningBoarderLoginField() == "rgba(187, 37, 37, 1)"
    app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()


def test_emptyPassword(app):
    app.session.login(LoginCred(username="triced", password=""))
    app.session.captchaEntering()
    assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
    assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"
    assert app.warning.warrningBoarderLoginField() == "rgba(187, 37, 37, 1)"
    app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()


def test_loginNotExistUser(app):
    app.session.login(LoginCred(username="triced" + str(random), password="TestTest12"))
    assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
    assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"
    assert app.warning.warrningBoarderLoginField() == "rgba(187, 37, 37, 1)"
    app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()

def test_nickNameWithDoteAfter(app):
    app.session.login(LoginCred(username="triced.", password="TestTest12"))
    app.session.captchaEntering()
    assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
    assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"
    assert app.warning.warrningBoarderLoginField() == "rgba(187, 37, 37, 1)"
    app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()

def test_emailWithDoteAfter(app):
    app.session.login(LoginCred(username="triced8+3030@gmail.com.", password="TestTest12"))
    app.session.captchaEntering()

    assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
    assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"
    assert app.warning.warrningBoarderLoginField() == "rgba(187, 37, 37, 1)"
    app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()

def test_nickNameWithDoteBefore(app):
    app.session.login(LoginCred(username=".triced", password="TestTest12"))
    app.session.captchaEntering()
    assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
    assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"
    assert app.warning.warrningBoarderLoginField() == "rgba(187, 37, 37, 1)"
    app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()

def test_loginPasswordCaps(app):
    app.session.login(LoginCred(username="triced8+3030@gmail.com", password="TestTest12".upper()))
    app.session.captchaEntering()
    assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
    assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"
    assert app.warning.warrningBoarderLoginField() == "rgba(187, 37, 37, 1)"
    app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()