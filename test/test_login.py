import time
from model.credLogin import LoginCred
from random import randrange

random = randrange(100000)

def test_loginNick(app):
    app.session.login(LoginCred(username="triced", password="TestTest12"))
    app.session.ensureLogin(username="triced")
    app.session.logout()

def test_loginNickSpaceAfter(app):
    app.session.login(LoginCred(username="triced ", password="TestTest12"))
    app.session.ensureLogin(username="triced")
    app.session.logout()

def test_loginNickSpaceBefore(app):
    app.session.login(LoginCred(username=" triced", password="TestTest12"))
    app.session.ensureLogin(username="triced")
    app.session.logout()

def test_loginEmail(app):
    app.session.login(LoginCred(username="triced8+3030@gmail.com", password="TestTest12"))
    app.session.ensureLogin(username="tricedu")
    app.session.logout()

def test_loginEmailCaps(app):
    app.session.login(LoginCred(username="triced8+3030@gmail.com".upper(), password="TestTest12"))
    app.session.ensureLogin(username="tricedu")
    app.session.logout()
"""
def test_emptyFields(app):
    app.session.login(LoginCred(username="", password=""))
    time.sleep(1)
    app.session.blabla()
    assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
    assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"
    assert app.warning.warrningBoarderLoginField() == "rgba(187, 37, 37, 1)"
    app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()

def test_emptyUserName(app):
    app.session.login(LoginCred(username="", password="TestTest12"))
    time.sleep(1)
    app.session.blabla()
    assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
    assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"
    assert app.warning.warrningBoarderLoginField() == "rgba(187, 37, 37, 1)"
    app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()


def test_emptyPassword(app):
    app.session.login(LoginCred(username="triced", password=""))
    time.sleep(1)
    app.session.blabla()
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
    time.sleep(1)
    app.session.blabla()
    assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
    assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"
    assert app.warning.warrningBoarderLoginField() == "rgba(187, 37, 37, 1)"
    app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()

def test_emailWithDoteAfter(app):
    app.session.login(LoginCred(username="triced8+3030@gmail.com.", password="TestTest12"))
    time.sleep(1)
    app.session.blabla()
    #assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
    #assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"
    #assert app.warning.warrningBoarderLoginField() == "rgba(187, 37, 37, 1)"
    app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()

def test_nickNameWithDoteBefore(app):
    app.session.login(LoginCred(username=".triced", password="TestTest12"))
    time.sleep(1)
    app.session.blabla()

    #assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
    #assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"
    #assert app.warning.warrningBoarderLoginField() == "rgba(187, 37, 37, 1)"
    app.driver.find_element_by_xpath("//div[@id='login']//button[@aria-label='Close']").click()
"""
def test_seePasword(app):
    app.session.fillFieldsSeePasword(LoginCred(username="triced", password="TestTest12"))
    assert app.warning.passswordFieldGetValue() == "TestTest12"

#def test_openadmin(app):
#    app.session.login(LoginCred(username="tricedu", password="TestTest12"))
#    time.sleep(0.1)
#    app.admin.open()











"""
def test_login(app):
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.session.login(LoginCred(username="triced", password="TestTest12"))
        app.session.ensureLogin(username="triced", password="TestTest12")
        app.session.logout()
        #time.sleep(10)

def test_emptyFields(app):
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.session.login(LoginCred(username="", password=""))
        assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
        assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"
        assert app.warning.warrningBoarderLoginField() == "rgba(187, 37, 37, 1)"

def test_emptyUserName(app):
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.session.login(LoginCred(username="", password="TestTest12"))
        assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
        assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"
        assert app.warning.warrningBoarderLoginField() == "rgba(187, 37, 37, 1)"


def test_emptyPassword(app):
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.session.login(LoginCred(username="triced", password=""))
        assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
        assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"
        assert app.warning.warrningBoarderLoginField() == "rgba(187, 37, 37, 1)"


def test_loginNotExistUser(app):
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.session.login(LoginCred(username="triced" + str(random), password="TestTest12"))
        assert app.warning.warrningMessageFromLoginPopUp() == "Почта или пароль указаны неверно"
        assert app.warning.warrningBoarderPasswordField() == "rgba(187, 37, 37, 1)"
        assert app.warning.warrningBoarderLoginField() == "rgba(187, 37, 37, 1)"


def test_openadmin(app):
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.session.login(LoginCred(username="tricedu", password="TestTest12"))
        time.sleep(0.1)
        app.admin.open()
"""
