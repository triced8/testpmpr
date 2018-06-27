import time
from model.credSignup import SignupCred
from model.credLogin import LoginCred
from random import randrange
random = randrange(100000)



"""
def test_signUpEmpty(app):
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUp(SignupCred(email = "", username = "" + str(random), password = "", captcha = ""))
    assert
"""