import time
from model.credSignup import SignupCred
from model.credLogin import LoginCred
from random import randrange
random = randrange(100000)




def test_signUpEmpty(app):
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUp(SignupCred(email="", username="", password="", captcha=""))
    assert app.warning.warningMessage(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][1]") == "Поле обязательно для заполнения"
    assert app.warning.warningMessage(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][1]") == "Поле обязательно для заполнения"
    assert app.warning.warningMessage(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'password'][1]") == "Поле обязательно для заполнения"
    assert app.warning.warningMessage(
        "//div[@id='registration']//div[@class='modala-captcha__wrapper']/span[1]") == "Поле обязательно для заполнения"

    assert app.warning.warrningBoarder("//div[@id='registration']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    assert app.warning.warrningBoarder("//input[@name='email']") == "rgba(187, 37, 37, 1)"
    assert app.warning.warrningBoarder("//input[@name='nick']") == "rgba(187, 37, 37, 1)"
    assert app.warning.warrningBoarder("//div[@id='registration']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    assert app.warning.warrningBoarder("//div[@id='registration']//input[@name='captcha']") == "rgba(187, 37, 37, 1)"
