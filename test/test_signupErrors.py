import time
from model.credSignup import SignupCred
from random import randrange

random = randrange(100000000)


def test_sign_up_empty(app):
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(SignupCred(email="", username="", password="", captcha=""))

    if app.registration.error_sign_up():
        test_sign_up_empty(app)
    # Turn off PP check box
    app.driver.find_element_by_xpath(
        "//div[@id='registration']//div[@class='modala__agreement_wrapper']//span[@class='checkbox__box']").click()
    time.sleep(0.5)
    # Error message for email field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][1]") == "Поле обязательно для заполнения"
    # Error message for NickName field
    assert app.warning.get_outer_text(
        "//form[@action='/profile/create/']/div[2]/span[3]") == "Поле обязательно для заполнения"
    # Error message for password field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'password'][1]") == "Поле обязательно для заполнения"
    # Error message for PP captcha
    assert app.warning.get_outer_text(
        "//div[@id='registration']//div[6]//span[@class='modala__error']") == "Поле обязательно для заполнения"
    # Error message for captcha field
    assert app.warning.get_outer_text(
        "//div[@class='modala-captcha__wrapper']/span[1]") == "Поле обязательно для заполнения"
    # Border for email field
    assert app.warning.get_border_color("//input[@name='email']") == "rgba(187, 37, 37, 1)"
    # Border for nickname field
    assert app.warning.get_border_color("//input[@name='nick']") == "rgba(187, 37, 37, 1)"
    # Border for password field
    assert app.warning.get_border_color(
        "//div[@id='registration']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    # Border for PP check box field
    assert app.warning.get_border_color("//*[@id='registration']//div[6]/div") == "rgba(187, 37, 37, 1)"
    # Border for captcha field
    assert app.warning.get_border_color("//div[@id='registration']//input[@name='captcha']") == "rgba(187, 37, 37, 1)"


def test_sign_up_empty_email(app):
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="", username="triced" + str(random), password="TestTest12", captcha="1111"))
    # Error message for email field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][1]") == "Поле обязательно для заполнения"
    # Border for email field
    assert app.warning.get_border_color("//input[@name='email']") == "rgba(187, 37, 37, 1)"


def test_sign_up_empty_nick(app):
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="", password="TestTest12",
                       captcha="1111"))
    # Error message for NickName field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][1]") == "Поле обязательно для заполнения"
    # Border for nickname field
    assert app.warning.get_border_color("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


def test_sign_up_empty_password(app):
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random), password="",
                       captcha="1111"))
    # Error message for password field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'password'][1]") == "Поле обязательно для заполнения"
    # Border for password field
    assert app.warning.get_border_color(
        "//div[@id='registration']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"


def test_sign_up_empty_pp_checkbox(app):
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random),
                       password="TestTest12", captcha="1111"))
    # Turn off PP check box
    app.driver.find_element_by_xpath(
        "//div[@id='registration']//div[@class='modala__agreement_wrapper']//span[@class='checkbox__box']").click()
    # Error message for PP captcha
    assert app.warning.get_outer_text(
        "//div[@id='registration']//div[6]//span[@class='modala__error']") == "Поле обязательно для заполнения"
    # Border for PP check box field
    assert app.warning.get_border_color("//*[@id='registration']//div[6]/div") == "rgba(187, 37, 37, 1)"


def test_sign_up_captcha(app):
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random),
                       password="TestTest12", captcha=""))
    # Error message for captcha field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//div[@class='modala-captcha__wrapper']/span[1]") == "Поле обязательно для заполнения"
    # Border for captcha field
    assert app.warning.get_border_color("//div[@id='registration']//input[@name='captcha']") == "rgba(187, 37, 37, 1)"


def test_signup_with_exist_email(app):
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="testpm8+3232@gmail.com", username="triced" + str(random), password="TestTest12",
                       captcha="1111"))
        time.sleep(0.1)
    # Error message for email field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][3]") == "Этот email уже зарегистрирован"
    # Border for email field
    assert app.warning.get_border_color("//input[@name='email']") == "rgba(187, 37, 37, 1)"


def test_signup_without_AT(app):
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="testpm8+3232gmail.com", username="triced" + str(random), password="TestTest12",
                       captcha="1111"))
        time.sleep(0.1)
    # Error message for email field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][4]") == "Неверный ввод"
    # Border for email field
    assert app.warning.get_border_color("//input[@name='email']") == "rgba(187, 37, 37, 1)"


def test_signup_without_domain(app):
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="testpm8+3232@.com", username="triced" + str(random), password="TestTest12",
                       captcha="1111"))
        time.sleep(0.1)
    # Error message for email field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][4]") == "Неверный ввод"
    # Border for email field
    assert app.warning.get_border_color("//input[@name='email']") == "rgba(187, 37, 37, 1)"


def test_signup_without_email_name(app):
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="@gmail.com", username="triced" + str(random), password="TestTest12", captcha="1111"))
        time.sleep(0.1)
    # Error message for email field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][4]") == "Неверный ввод"
    # Border for email field
    assert app.warning.get_border_color("//input[@name='email']") == "rgba(187, 37, 37, 1)"
    app.driver.quit()


def test_signup_without_dot_com(app):
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="pmtest8+3232@gmail", username="triced" + str(random), password="TestTest12",
                       captcha="1111"))
        time.sleep(0.1)
    # Error message for email field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][4]") == "Неверный ввод"
    # Border for email field
    assert app.warning.get_border_color("//input[@name='email']") == "rgba(187, 37, 37, 1)"


def test_signup_without_dot(app):
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="pmtest8+3232@gmailcom", username="triced" + str(random), password="TestTest12",
                       captcha="1111"))
        time.sleep(0.1)
    # Error message for email field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][4]") == "Неверный ввод"
    # Border for email field
    assert app.warning.get_border_color("//input[@name='email']") == "rgba(187, 37, 37, 1)"


def test_signup_exist_nick(app):
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="tricedu", password="TestTest12",
                       captcha="1111"))
    # Error message for NickName field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][4]") == "Этот логин уже занят"
    # Border for nickname field
    assert app.warning.get_border_color("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


def test_sign_up_nick_space_middle(app):
    random = randrange(1000000000)
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + " " + str(random),
                       password="TestTest12", captcha="1111"))
    # Error message for NickName field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][3]") == "Разрешены только a-z, 0-9 и _ символы"
    # Border for nickname field
    assert app.warning.get_border_color("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


def test_sign_up_nick_with_special(app):
    random = randrange(1000000000)
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced+" + str(random),
                       password="TestTest12", captcha="1111"))
    # Error message for NickName field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][3]") == "Разрешены только a-z, 0-9 и _ символы"
    # Border for nickname field
    assert app.warning.get_border_color("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


def test_sign_up_nick_min(app):
    random = randrange(1000000000)
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="T", password="TestTest12",
                       captcha="1111"))
    # Error message for NickName field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][2]") == "Логин слишком короткий"
    # Border for nickname field
    assert app.warning.get_border_color("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


def test_sign_up_nick_space_before(app):
    random = randrange(1000000000)
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="testpm8+" + str(random) + "@gmail.com", username=" triced" + str(random),
                       password="TestTest12", captcha="1111"))
    # Error message for NickName field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][3]") == "Разрешены только a-z, 0-9 и _ символы"
    # Border for nickname field
    assert app.warning.get_border_color("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


def test_sign_up_nick_space_all(app):
    random = randrange(1000000000)
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="        " + str(random),
                       password="TestTest12", captcha="1111"))
    # Error message for NickName field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][3]") == "Разрешены только a-z, 0-9 и _ символы"
    # Border for nickname field
    assert app.warning.get_border_color("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


def test_sign_up_password_empty(app):
    random = randrange(1000000000)
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random), password="",
                       captcha="1111"))
    # Error message for password field
    assert app.warning.get_outer_text(
        "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'password'][1]") == "Поле обязательно для заполнения"
    # Border for password field
    assert app.warning.get_border_color(
        "//div[@id='registration']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"


def test_sign_up_password_wrong_captcha(app):
    random = randrange(1000000000)
    if app.session.user_logged():
        app.open_main_page_ru()
        app.session.logout()
    else:
        app.registration.sign_up(
            SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random),
                       password="TestTest12",
                       captcha="1234"))
    # Error message for captcha field
    assert app.warning.get_outer_text(
        "//div[@class='modala-captcha__wrapper']/span[2]") == "Введено неверное значение"
    # Border for captcha field
    assert app.warning.get_border_color("//div[@id='registration']//input[@name='captcha']") == "rgba(187, 37, 37, 1)"
