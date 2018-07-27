import time
from model.credSignup import SignupCred
from model.credLogin import LoginCred
from random import randrange
random = None

"""
def test_signUp(app):
    random = randrange(1000000000)
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUp(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random), password = "TestTest12", captcha = "1111"))
"""


def test_signUpHeppyPass(app):
    random = randrange(1000000000)
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUpHeppyPass(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random), password = "TestTest12", captcha = "1111"))
    assert app.warning.getOuterText("//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"


def test_signUpWithSpaceBefore(app):
    random = randrange(1000000000)
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUpHeppyPass(SignupCred(email = " testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random), password = "TestTest12", captcha = "1111"))
    assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

def test_signUpWithSpaceAfter(app):
    random = randrange(1000000000)
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUpHeppyPass(SignupCred(email = "testpm8+" + str(random) + "@gmail.com ", username = "triced" + str(random), password = "TestTest12", captcha = "1111"))
    assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

def test_signUpNickUpper(app):
    random = randrange(1000000000)
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUpHeppyPass(SignupCred(email = ("testpm8+" + str(random) + "@gmail.com ").upper(), username = ("triced" + str(random)).upper(), password = "TestTest12", captcha = "1111"))
    assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

def test_signUpNickSpaceAfter(app):
    random = randrange(1000000000)
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUpHeppyPass(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random) + " ", password = "TestTest12", captcha = "1111"))
    assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

def test_signUpNickNumberOnly(app):
    random = randrange(1000000000)
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUpHeppyPass(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = str(random), password = "TestTest12", captcha = "1111"))
    assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

def test_signUpPasswordUpper(app):
    random = randrange(1000000000)
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUpHeppyPass(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random), password = ("TestTest12").upper(), captcha = "1111"))
    assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

def test_signUpPasswordLow(app):
    random = randrange(1000000000)
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUpHeppyPass(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random), password = ("TestTest12").lower(), captcha = "1111"))
    assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

def test_signUpPasswordNumber(app):
    random = randrange(1000000000)
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUpHeppyPass(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random), password = "123456789", captcha = "1111"))
    assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

def test_signUpPasswordSpecial(app):
    random = randrange(1000000000)
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUpHeppyPass(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random), password = '!@#$%^/\&*()~?|}"\'{:[]<>,.', captcha = "1111"))
    assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

def test_signUpPasswordSeePassword(app):
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.openSignupPopup()
    app.driver.find_element_by_xpath("(//input[@name='password'])[4]").send_keys("TestTest12")
    app.driver.find_element_by_xpath("//div[@id='registration']//span[@class='switch_pass']").click()
    assert app.warning.getValue(xpath="(//input[@name='password'])[4]") == "TestTest12"
    assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

def test_closeOutside(app):
    app.registration.openSignupPopup()
    app.session.clickOutSide()
    assert not app.session.elementIsDisplay("//div[@id='registration']//h4[@class='modala__title']")