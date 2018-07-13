import time
from model.credLogin import LoginCred
from random import randrange

random = randrange(100000)

def test_loginNick(app):
    app.session.login(LoginCred(username="triced", password="TestTest12"))
    assert len(app.driver.find_elements_by_xpath("//a[@href='https://beta.pokermatch.com/ru/page/cash']")) > 0
    app.session.ensureLogin(username="triced")
    app.session.logout()


def test_loginNickSpaceAfter(app):
    app.session.login(LoginCred(username="triced ", password="TestTest12"))
    assert len(app.driver.find_elements_by_xpath("//a[@href='https://beta.pokermatch.com/ru/page/cash']")) > 0
    app.session.ensureLogin(username="triced")
    app.session.logout()

def test_loginNickSpaceBefore(app):
    app.session.login(LoginCred(username=" triced", password="TestTest12"))
    assert len(app.driver.find_elements_by_xpath("//a[@href='https://beta.pokermatch.com/ru/page/cash']")) > 0
    app.session.ensureLogin(username="triced")
    app.session.logout()

def test_loginEmail(app):
    app.session.login(LoginCred(username="triced8+3030@gmail.com", password="TestTest12"))
    assert len(app.driver.find_elements_by_xpath("//a[@href='https://beta.pokermatch.com/ru/page/cash']")) > 0
    app.session.ensureLogin(username="tricedu")
    app.session.logout()

def test_loginEmailCaps(app):
    app.session.login(LoginCred(username="triced8+3030@gmail.com".upper(), password="TestTest12"))
    assert len(app.driver.find_elements_by_xpath("//a[@href='https://beta.pokermatch.com/ru/page/cash']")) > 0
    app.session.ensureLogin(username="tricedu")
    app.session.logout()

def test_loginNickCaps(app):
    app.session.login(LoginCred(username="tricedu".upper(), password="TestTest12"))
    assert len(app.driver.find_elements_by_xpath("//a[@href='https://beta.pokermatch.com/ru/page/cash']")) > 0
    app.session.ensureLogin(username="tricedu")
    app.session.logout()

def test_closeOutside(app):
    app.session.openLoginPopup()
    app.session.clickOutSide()
    assert not app.session.elementIsDisplay("//form[@action='/login/']//div[@class='modala-button__text']")


def test_seePasword(app):
    app.session.fillFieldsSeePasword(LoginCred(username="triced", password="TestTest12"))
    assert app.warning.getValue(xpath="(//input[@name='password'])[2]") == "TestTest12"

#def test_openadmin(app):
#    app.session.login(LoginCred(username="tricedu", password="TestTest12"))
#    time.sleep(0.1)
#    app.admin.open()
