import time
from model.credSignup import SignupCred
from random import randrange
random = randrange(100000)


def test_signUp(app):
    app.registration.signUp(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random), password = "TestTest12", captcha = "1111"))
