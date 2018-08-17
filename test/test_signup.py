import time
from model.credSignup import SignupCred
import pytest
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

@pytest.allure.step("Signup with happy pass")
def test_signUpHappyPass(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.userLogged():
            app.openMainPageRu()
            app.session.logout()
        else:
            with pytest.allure.step("Fill in form by valid data"):
                app.registration.signUpHeppyPass(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random), password = "TestTest12", captcha = "1111"))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.getOuterText("//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

@pytest.allure.step("Signup with space before email")
def test_signUpWithSpaceBefore(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.userLogged():
            app.openMainPageRu()
            app.session.logout()
        else:
            with pytest.allure.step("Sign up with space before email"):
                app.registration.signUpHeppyPass(SignupCred(email = " testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random), password = "TestTest12", captcha = "1111"))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

@pytest.allure.step("Signup with space after email")
def test_signUpWithSpaceAfter(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.userLogged():
            app.openMainPageRu()
            app.session.logout()
        else:
            with pytest.allure.step("Sign up with space after email"):
                app.registration.signUpHeppyPass(SignupCred(email = "testpm8+" + str(random) + "@gmail.com ", username = "triced" + str(random), password = "TestTest12", captcha = "1111"))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

@pytest.allure.step("Signup with nick name caps")
def test_signUpNickEmailUpper(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.userLogged():
            app.openMainPageRu()
            app.session.logout()
        else:
            with pytest.allure.step("Sign up with email and nick upper"):
                app.registration.signUpHeppyPass(SignupCred(email = ("testpm8+" + str(random) + "@gmail.com ").upper(), username = ("triced" + str(random)).upper(), password = "TestTest12", captcha = "1111"))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

@pytest.allure.step("Signup with space after nickname")
def test_signUpNickSpaceAfter(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.userLogged():
            app.openMainPageRu()
            app.session.logout()
        else:
            with pytest.allure.step("Sign up with space after nickname"):
                app.registration.signUpHeppyPass(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random) + " ", password = "TestTest12", captcha = "1111"))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

@pytest.allure.step("Signup with nick name number only")
def test_signUpNickNumberOnly(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.userLogged():
            app.openMainPageRu()
            app.session.logout()
        else:
            with pytest.allure.step("Signup with nick name number only"):
                app.registration.signUpHeppyPass(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = str(random), password = "TestTest12", captcha = "1111"))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

@pytest.allure.step("Signup with password caps")
def test_signUpPasswordUpper(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.userLogged():
            app.openMainPageRu()
            app.session.logout()
        else:
            with pytest.allure.step("Signup with password caps"):
                app.registration.signUpHeppyPass(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random), password = ("TestTest12").upper(), captcha = "1111"))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

@pytest.allure.step("Signup with password Low")
def test_signUpPasswordLow(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.userLogged():
            app.openMainPageRu()
            app.session.logout()
        else:
            with pytest.allure.step("Signup with password low"):
                app.registration.signUpHeppyPass(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random), password = ("TestTest12").lower(), captcha = "1111"))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

@pytest.allure.step("Signup with password only number")
def test_signUpPasswordNumber(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.userLogged():
            app.openMainPageRu()
            app.session.logout()
        else:
            with pytest.allure.step("Signup with password only number"):
                app.registration.signUpHeppyPass(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random), password = "123456789", captcha = "1111"))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

@pytest.allure.step("Signup with password only special symbols")
def test_signUpPasswordSpecial(app):
    random = randrange(1000000000)
    with pytest.allure.step("Log out if user is logged"):
        if app.session.userLogged():
            app.openMainPageRu()
            app.session.logout()
        else:
            with pytest.allure.step("Signup with password only special symbols"):
                app.registration.signUpHeppyPass(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random), password = '!@#$%^/\&*()~?|}"\'{:[]<>,.', captcha = "1111"))
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

@pytest.allure.step("See password button")
def test_signUpPasswordSeePassword(app):
    with pytest.allure.step("Log out if user is logged"):
        if app.session.userLogged():
            app.openMainPageRu()
            app.session.logout()
        else:
            with pytest.allure.step("Open signup pop-up"):
                app.registration.openSignupPopup()
    with pytest.allure.step("Fill in password field"):
        app.driver.find_element_by_xpath("(//input[@name='password'])[4]").send_keys("TestTest12")
    with pytest.allure.step("Click on the 'see password' button"):
        app.driver.find_element_by_xpath("//div[@id='registration']//span[@class='switch_pass']").click()
        assert app.warning.getValue(xpath="(//input[@name='password'])[4]") == "TestTest12"
    with pytest.allure.step("Assert for text about email"):
        assert app.warning.getOuterText(
        "//div[@class='event_message']") == "Вам было отправлено письмо для подтверждения регистрации, пожалуйста, подтвердите регистрацию в течение 24ч"

@pytest.allure.step("Close pop-up by outside click")
def test_closeOutside(app):
    with pytest.allure.step("Open 'sign up' pop-up"):
        app.registration.openSignupPopup()
    with pytest.allure.step("Click out side pop-up"):
        app.session.clickOutSide()
    with pytest.allure.step("Asser that pup-up is closed"):
        assert not app.session.elementIsDisplay("//div[@id='registration']//h4[@class='modala__title']")