import time
from model.credSignup import SignupCred
from random import randrange
random = randrange(100000000)


def test_signUpEmpty(app):
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUp(SignupCred(email="", username="", password="", captcha=""))

    if app.registration.errorSignUp():
        test_signUpEmpty(app)
    # Turn off PP check box
    app.driver.find_element_by_xpath(
        "//div[@id='registration']//div[@class='modala__agreement_wrapper']//span[@class='checkbox__box']").click()
    time.sleep(0.5)
    # Error message for email field
    assert app.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][1]") == "Поле обязательно для заполнения"
    # Error message for NickName field
    assert app.warning.getOuterText(
        "//form[@action='/profile/create/']/div[2]/span[3]") == "Поле обязательно для заполнения"
    # Error message for password field
    assert app.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'password'][1]") == "Поле обязательно для заполнения"
    # Error message for PP captcha
    assert app.warning.getOuterText(
        "//div[@id='registration']//div[6]//span[@class='modala__error']") == "Поле обязательно для заполнения"
    # Error message for captcha field
    assert app.warning.getOuterText(
        "//div[@class='modala-captcha__wrapper']/span[1]") == "Поле обязательно для заполнения"
    # Border for email field
    assert app.warning.getBorderColor("//input[@name='email']") == "rgba(187, 37, 37, 1)"
    # Border for nickname field
    assert app.warning.getBorderColor("//input[@name='nick']") == "rgba(187, 37, 37, 1)"
    # Border for password field
    assert app.warning.getBorderColor(
        "//div[@id='registration']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    # Border for PP check box field
    assert app.warning.getBorderColor("//*[@id='registration']//div[6]/div") == "rgba(187, 37, 37, 1)"
    # Border for captcha field
    assert app.warning.getBorderColor("//div[@id='registration']//input[@name='captcha']") == "rgba(187, 37, 37, 1)"




def test_signUpEmptyEmail(app):
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUp(
            SignupCred(email="", username="triced" + str(random), password="TestTest12", captcha="1111"))
    """
    if app.registration.errorSignUp():
        app.driver.get("https://beta.pokermatch.com/ru#registration")
        test_signUpEmptyEmail(app)
    """
    # Error message for email field
    assert app.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][1]") == "Поле обязательно для заполнения"
    # Border for email field
    assert app.warning.getBorderColor("//input[@name='email']") == "rgba(187, 37, 37, 1)"


def test_signUpEmptyNick(app):
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUp(
            SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="", password="TestTest12",
                       captcha="1111"))
    """
    if app.registration.errorSignUp():
        app.driver.get("https://beta.pokermatch.com/ru#registration")
        test_signUpEmptyNick(app)
    """
    # Error message for NickName field
    assert app.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][1]") == "Поле обязательно для заполнения"
    # Border for nickname field
    assert app.warning.getBorderColor("//input[@name='nick']") == "rgba(187, 37, 37, 1)"

def test_signUpEmptyPassword(app):
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUp(
            SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random), password="",
                       captcha="1111"))
    """   
    if app.registration.errorSignUp():
        app.driver.get("https://beta.pokermatch.com/ru#registration")
        test_signUpEmptyPassword(app)
    """
    # Error message for password field
    assert app.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'password'][1]") == "Поле обязательно для заполнения"
    # Border for password field
    assert app.warning.getBorderColor(
        "//div[@id='registration']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"


def test_signUpEmptyPPCheckBox(app):
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUp(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random), password = "TestTest12", captcha = "1111"))
    # Turn off PP check box
    app.driver.find_element_by_xpath(
        "//div[@id='registration']//div[@class='modala__agreement_wrapper']//span[@class='checkbox__box']").click()
    """
    if app.registration.errorSignUp():
        app.driver.get("https://beta.pokermatch.com/ru#registration")
        test_signUpEmptyPPCheckBox(app)
    """
    # Error message for PP captcha
    assert app.warning.getOuterText(
        "//div[@id='registration']//div[6]//span[@class='modala__error']") == "Поле обязательно для заполнения"
    # Border for PP check box field
    assert app.warning.getBorderColor("//*[@id='registration']//div[6]/div") == "rgba(187, 37, 37, 1)"


def test_signUpCaptcha(app):
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUp(
            SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random),
                       password="TestTest12", captcha=""))
    """
    if app.registration.errorSignUp():
        app.driver.get("https://beta.pokermatch.com/ru#registration")
        test_signUpCaptcha(app)
    """
    # Error message for captcha field
    assert app.warning.getOuterText(
        "//div[@id='registration']//div[@class='modala-captcha__wrapper']/span[1]") == "Поле обязательно для заполнения"
    # Border for captcha field
    assert app.warning.getBorderColor("//div[@id='registration']//input[@name='captcha']") == "rgba(187, 37, 37, 1)"


def test_signupWithExistEmail(app):
    if app.session.userLogged():
        app.openMainPageRu()
        app.session.logout()
    else:
        app.registration.signUp(SignupCred(email = "testpm8+3232@gmail.com", username = "triced" + str(random), password = "TestTest12", captcha = "1111"))
        time.sleep(0.1)
    """
    if app.registration.errorSignUp():
        app.driver.get("https://beta.pokermatch.com/ru#registration")
        test_signupWithExistEmail(app)
    """
    # Error message for email field
    assert app.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][3]") == "Этот email уже зарегистрирован"
    # Border for email field
    assert app.warning.getBorderColor("//input[@name='email']") == "rgba(187, 37, 37, 1)"


def test_signupWithoutAT(app1):
    if app1.session.userLogged():
        app1.openMainPageRu()
        app1.session.logout()
    else:
        app1.registration.signUp(SignupCred(email = "testpm8+3232gmail.com", username = "triced" + str(random), password = "TestTest12", captcha = "1111"))
        time.sleep(0.1)
    """
    if app.registration.errorSignUp():
        app.driver.get("https://beta.pokermatch.com/ru#registration")
        test_signupWithoutAT(app)
    """
    # Error message for email field
    assert app1.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][4]") == "Неверный ввод"
    # Border for email field
    assert app1.warning.getBorderColor("//input[@name='email']") == "rgba(187, 37, 37, 1)"


def test_signupWithoutDomain(app1):
    if app1.session.userLogged():
        app1.openMainPageRu()
        app1.session.logout()
    else:
        app1.registration.signUp(SignupCred(email = "testpm8+3232@.com", username = "triced" + str(random), password = "TestTest12", captcha = "1111"))
        time.sleep(0.1)
    """
    if app.registration.errorSignUp():
        app.driver.get("https://beta.pokermatch.com/ru#registration")
        test_signupWithoutDomain(app)
    """
    # Error message for email field
    assert app1.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][4]") == "Неверный ввод"
    # Border for email field
    assert app1.warning.getBorderColor("//input[@name='email']") == "rgba(187, 37, 37, 1)"


def test_signupWithoutEmailName(app1):
    if app1.session.userLogged():
        app1.openMainPageRu()
        app1.session.logout()
    else:
        app1.registration.signUp(SignupCred(email = "@gmail.com", username = "triced" + str(random), password = "TestTest12", captcha = "1111"))
        time.sleep(0.1)
    """
    if app.registration.errorSignUp():
        app.driver.get("https://beta.pokermatch.com/ru#registration")
        test_signupWithoutEmailName(app)
    """
    # Error message for email field
    assert app1.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][4]") == "Неверный ввод"
    # Border for email field
    assert app1.warning.getBorderColor("//input[@name='email']") == "rgba(187, 37, 37, 1)"


def test_signupWithoutDotCom(app1):
    if app1.session.userLogged():
        app1.openMainPageRu()
        app1.session.logout()
    else:
        app1.registration.signUp(SignupCred(email = "pmtest8+3232@gmail", username = "triced" + str(random), password = "TestTest12", captcha = "1111"))
        time.sleep(0.1)
    """
    if app.registration.errorSignUp():
        app.driver.refresh()
        #app.driver.get("https://beta.pokermatch.com/ru#registration")
        test_signupWithoutDotCom(app)
    """
    # Error message for email field
    assert app1.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][4]") == "Неверный ввод"
    # Border for email field
    assert app1.warning.getBorderColor("//input[@name='email']") == "rgba(187, 37, 37, 1)"


def test_signupWithoutDot(app1):
    if app1.session.userLogged():
        app1.openMainPageRu()
        app1.session.logout()
    else:
        app.registration.signUp(SignupCred(email = "pmtest8+3232@gmailcom", username = "triced" + str(random), password = "TestTest12", captcha = "1111"))
        time.sleep(0.1)
    """
    if app.registration.errorSignUp():
        app.driver.get("https://beta.pokermatch.com/ru#registration")
        test_signupWithoutDot(app)
    """
    # Error message for email field
    assert app1.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][4]") == "Неверный ввод"
    # Border for email field
    assert app1.warning.getBorderColor("//input[@name='email']") == "rgba(187, 37, 37, 1)"


def test_signupExistNick(app1):
    if app1.session.userLogged():
        app1.openMainPageRu()
        app1.session.logout()
    else:
        app1.registration.signUp(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "tricedu", password = "TestTest12", captcha = "1111"))
    """
    if app.registration.errorSignUp():
        app.driver.get("https://beta.pokermatch.com/ru#registration")
        test_signupExistNick(app)
    """
    # Error message for NickName field
    assert app1.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][4]") == "Этот логин уже занят"
    # Border for nickname field
    assert app1.warning.getBorderColor("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


def test_signUpNickSpaceMiddle(app1):
    random = randrange(1000000000)
    if app1.session.userLogged():
        app1.openMainPageRu()
        app1.session.logout()
    else:
        app1.registration.signUp(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + " " + str(random), password = "TestTest12", captcha = "1111"))
    """
    if app.registration.errorSignUp():
        app.driver.get("https://beta.pokermatch.com/ru#registration")
        test_signUpNickSpaceMiddle(app)
    """
    # Error message for NickName field
    assert app1.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][3]") == "Разрешены только a-z, 0-9 и _ символы"
    # Border for nickname field
    assert app1.warning.getBorderColor("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


def test_signUpNickWithSpecial(app1):
    random = randrange(1000000000)
    if app1.session.userLogged():
        app1.openMainPageRu()
        app1.session.logout()
    else:
        app1.registration.signUp(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced+" +  str(random), password = "TestTest12", captcha = "1111"))
    """
    if app.registration.errorSignUp():
        app.driver.get("https://beta.pokermatch.com/ru#registration")
        test_signUpNickWithSpecial(app)
    """
    # Error message for NickName field
    assert app1.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][3]") == "Разрешены только a-z, 0-9 и _ символы"
    # Border for nickname field
    assert app1.warning.getBorderColor("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


def test_signUpNickMin(app1):
    random = randrange(1000000000)
    if app1.session.userLogged():
        app1.openMainPageRu()
        app1.session.logout()
    else:
        app1.registration.signUp(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "T", password = "TestTest12", captcha = "1111"))
    """
    if app.registration.errorSignUp():
        test_signUpNickMin(app)
    """
    # Error message for NickName field
    assert app1.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][2]") == "Логин слишком короткий"
    # Border for nickname field
    assert app1.warning.getBorderColor("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


def test_signUpNickSpaceBefore(app1):
    random = randrange(1000000000)
    if app1.session.userLogged():
        app1.openMainPageRu()
        app1.session.logout()
    else:
        app1.registration.signUp(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = " triced" + str(random), password = "TestTest12", captcha = "1111"))
    """
    if app.registration.errorSignUp():
        test_signUpNickSpaceBefore(app)
    """
    # Error message for NickName field
    assert app1.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][3]") == "Разрешены только a-z, 0-9 и _ символы"
    # Border for nickname field
    assert app1.warning.getBorderColor("//input[@name='nick']") == "rgba(187, 37, 37, 1)"

def test_signUpNickSpaceAll(app1):
    random = randrange(1000000000)
    if app1.session.userLogged():
        app1.openMainPageRu()
        app1.session.logout()
    else:
        app1.registration.signUp(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "        " + str(random), password = "TestTest12", captcha = "1111"))
    """
    if app.registration.errorSignUp():
        test_signUpNickSpaceBefore(app)
    """
    # Error message for NickName field
    assert app1.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][3]") == "Разрешены только a-z, 0-9 и _ символы"
    # Border for nickname field
    assert app1.warning.getBorderColor("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


def test_signUpPasswordEmpty(app1):
    random = randrange(1000000000)
    if app1.session.userLogged():
        app1.openMainPageRu()
        app1.session.logout()
    else:
        app1.registration.signUp(SignupCred(email = "testpm8+" + str(random) + "@gmail.com", username = "triced" + str(random), password = "", captcha = "1111"))
    # Error message for password field
    assert app1.warning.getOuterText(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'password'][1]") == "Поле обязательно для заполнения"
    # Border for password field
    assert app1.warning.getBorderColor(
        "//div[@id='registration']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"


def test_signUpPasswordWrongCaptcha(app1):
    random = randrange(1000000000)
    if app1.session.userLogged():
        app1.openMainPageRu()
        app1.session.logout()
    else:
        app1.registration.signUp(
            SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random), password="TestTest12",
                       captcha="1234"))
    # Error message for captcha field
    assert app1.warning.getOuterText(
        "//div[@class='modala-captcha__wrapper']/span[2]") == "Введено неверное значение"
    # Border for captcha field
    assert app1.warning.getBorderColor("//div[@id='registration']//input[@name='captcha']") == "rgba(187, 37, 37, 1)"