import time
from model.credLogin import LoginCred
from random import randrange

random = randrange(100000)


def test_login(app):
    app.session.login(LoginCred(username="triced", password="TestTest12"))
    app.session.ensureLogin(username="triced", password="TestTest12")
    app.session.logout()


def test_emptyFields(app):
    app.session.login(LoginCred(username="", password=""))
    #time.sleep(1)
    assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
    assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"


def test_emptyUserName(app):
    app.session.login(LoginCred(username="", password="TestTest12"))


def test_emptyPassword(app):
    app.session.login(LoginCred(username="triced", password=""))


def test_emptyNotExistUser(app):
    app.session.login(LoginCred(username="triced" + str(random), password="TestTest12"))


def test_openadmin(app):
    app.session.login(LoginCred(username="tricedu", password="TestTest12"))
    time.sleep(0.1)
    app.admin.open()
