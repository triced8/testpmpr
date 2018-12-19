import time
from model.credSignup import SignupCred
from random import randrange
import pytest
random = randrange(100000000)


@pytest.allure.step("Sign Up with empty fields")
def test_sign_up_empty(app):
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(SignupCred(email="", username="", password="", captcha="", promo_code=""))
    with pytest.allure.step("Turn off PP captcha"):
        app.driver.find_element_by_xpath(
            "//div[@id='registration']//div[@class='modala__agreement_wrapper']//span[@class='checkbox__box']").click()
        time.sleep(0.5)
    with pytest.allure.step("Check empty email field error"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][1]") == "Поле обязательно для заполнения"
    with pytest.allure.step("Check empty nickname field error"):
        assert app.warning.get_outer_text(
            "//form[@action='/profile/create/']/div[2]/span[3]") == "Поле обязательно для заполнения"
    with pytest.allure.step("Check empty password field error"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'password'][1]") == "Поле обязательно для заполнения"
    with pytest.allure.step("Error message for PP captcha"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//div[6]//span[@class='modala__error']") == "Поле обязательно для заполнения"
    with pytest.allure.step("Error message for captcha field"):
        assert app.warning.get_outer_text(
            "//div[@class='modala-captcha__wrapper']/span[1]") == "Поле обязательно для заполнения"
    with pytest.allure.step("Border for email field"):
        assert app.warning.get_border_color("//input[@name='email']") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Border for nickname field"):
        assert app.warning.get_border_color("//input[@name='nick']") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Border for password field"):
        assert app.warning.get_border_color(
            "//div[@id='registration']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Border for PP check box field"):
        assert app.warning.get_border_color("//*[@id='registration']//div[6]/div") == "rgba(187, 37, 37, 1)"
    with pytest.allure.step("Border for captcha field"):
        assert app.warning.get_border_color("//div[@id='registration']//input[@name='captcha']") == "rgba(187, 37, 37, 1)"


@pytest.allure.step("Sign Up with empty checkbox")
def test_sign_up_empty_pp_checkbox(app):
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random),
                           password="TestTest12", captcha="1111", promo_code=""))
    # Turn off PP check box
    app.driver.find_element_by_xpath(
        "//div[@id='registration']//div[@class='modala__agreement_wrapper']//span[@class='checkbox__box']").click()
    # Error message for PP captcha
    with pytest.allure.step("Error message for PP captcha"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//div[6]//span[@class='modala__error']") == "Поле обязательно для заполнения"
    # Border for PP check box field
    with pytest.allure.step("Border for PP checkbox"):
        assert app.warning.get_border_color("//*[@id='registration']//div[6]/div") == "rgba(187, 37, 37, 1)"


@pytest.allure.step("Sign Up with empty captcha field")
def test_sign_up_captcha(app):
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random),
                           password="TestTest12", captcha="", promo_code=""))
    # Error message for captcha field
    with pytest.allure.step("Check empty captcha field error"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//div[@class='modala-captcha__wrapper']/span[1]") == "Поле обязательно для заполнения"
    # Border for captcha field
    with pytest.allure.step("Border for captcha field"):
        assert app.warning.get_border_color("//div[@id='registration']//input[@name='captcha']") == "rgba(187, 37, 37, 1)"


@pytest.allure.step("Sign Up with exist email")
def test_signup_with_exist_email(app):
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="testpm8+3232@gmail.com", username="triced" + str(random), password="TestTest12",
                           captcha="1111", promo_code=""))
            time.sleep(0.1)
    # Error message for email field
    with pytest.allure.step("Error for exist email near email field"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][3]") == "Этот email уже зарегистрирован"
    # Border for email field
    with pytest.allure.step("Border for email field"):
        assert app.warning.get_border_color("//input[@name='email']") == "rgba(187, 37, 37, 1)"


@pytest.allure.step("Sign Up with wrong captcha")
def test_sign_up_password_wrong_captcha(app):
    random = randrange(1000000000)
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random),
                           password="TestTest12",
                           captcha="1234", promo_code=""))
    # Error message for captcha field
    with pytest.allure.step("Error with wrong captcha for captcha field"):
        assert app.warning.get_outer_text(
            "//div[@class='modala-captcha__wrapper']/span[2]") == "Введено неверное значение"
    # Border for captcha field
    with pytest.allure.step("Border for captcha field"):
        assert app.warning.get_border_color("//div[@id='registration']//input[@name='captcha']") == "rgba(187, 37, 37, 1)"


@pytest.allure.step("Sign Up with exist nickname")
def test_signup_exist_nick(app):
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="tricedu", password="TestTest12",
                           captcha="1111", promo_code=""))
    # Error message for NickName field
    with pytest.allure.step("Error with exist nickname for nickname field"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][4]") == "Этот логин уже занят"
    # Border for nickname field
    with pytest.allure.step("Border for nickname field"):
        assert app.warning.get_border_color("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


@pytest.allure.step("Sign Up with special symbols in the nickname")
def test_sign_up_nick_with_special(app):
    random = randrange(1000000000)
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced+" + str(random),
                           password="TestTest12", captcha="1111", promo_code=""))
    # Error message for NickName field
    with pytest.allure.step("Error with incorrect nickname for nickname field"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][3]") == "Разрешены только a-z, 0-9 и _ символы"
    # Border for nickname field
    with pytest.allure.step("Border for nickname field"):
        assert app.warning.get_border_color("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


"""
@pytest.allure.step("Sign Up without AT in email")
def test_signup_without_AT(app):
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="testpm8+3232gmail.com", username="triced" + str(random), password="TestTest12",
                           captcha="1111"))
        time.sleep(0.1)
    # Error message for email field
    with pytest.allure.step("Error with incorrect email for email field"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][4]") == "Неверный ввод"
    # Border for email field
    with pytest.allure.step("Border for email field"):
        assert app.warning.get_border_color("//input[@name='email']") == "rgba(187, 37, 37, 1)"


@pytest.allure.step("Sign Up without domain in email")
def test_signup_without_domain(app):
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="testpm8+3232@.com", username="triced" + str(random), password="TestTest12",
                           captcha="1111"))
            time.sleep(0.1)
    # Error message for email field
    with pytest.allure.step("Error with incorrect email for email field"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][4]") == "Неверный ввод"
    # Border for email field
    with pytest.allure.step("Border for email field"):
        assert app.warning.get_border_color("//input[@name='email']") == "rgba(187, 37, 37, 1)"


@pytest.allure.step("Sign Up without email name in email")
def test_signup_without_email_name(app):
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="@gmail.com", username="triced" + str(random), password="TestTest12", captcha="1111"))
            time.sleep(0.1)
    # Error message for email field
    with pytest.allure.step("Error with incorrect email for email field"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][4]") == "Неверный ввод"
    # Border for email field
    with pytest.allure.step("Border for email field"):
        assert app.warning.get_border_color("//input[@name='email']") == "rgba(187, 37, 37, 1)"



@pytest.allure.step("Sign Up without dot com in email")
def test_signup_without_dot_com(app):
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="pmtest8+3232@gmail", username="triced" + str(random), password="TestTest12",
                           captcha="1111"))
            time.sleep(0.1)
    # Error message for email field
    with pytest.allure.step("Error with incorrect email for email field"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][4]") == "Неверный ввод"
    # Border for email field
    with pytest.allure.step("Border for email field"):
        assert app.warning.get_border_color("//input[@name='email']") == "rgba(187, 37, 37, 1)"


@pytest.allure.step("Sign Up without dot in email")
def test_signup_without_dot(app):
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="pmtest8+3232@gmailcom", username="triced" + str(random), password="TestTest12",
                           captcha="1111"))
            time.sleep(0.1)
    # Error message for email field
    with pytest.allure.step("Error with incorrect email for email field"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][4]") == "Неверный ввод"
    # Border for email field
    with pytest.allure.step("Border for email field"):
        assert app.warning.get_border_color("//input[@name='email']") == "rgba(187, 37, 37, 1)"


@pytest.allure.step("Sign Up with space in the middle of nickname")
def test_sign_up_nick_space_middle(app):
    random = randrange(1000000000)
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + " " + str(random),
                           password="TestTest12", captcha="1111"))
    # Error message for NickName field
    with pytest.allure.step("Error with incorrect nickname for nickname field"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][3]") == "Разрешены только a-z, 0-9 и _ символы"
    # Border for nickname field
    with pytest.allure.step("Border for nickname field"):
        assert app.warning.get_border_color("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


@pytest.allure.step("Sign Up with one symbols as nickname")
def test_sign_up_nick_min(app):
    random = randrange(1000000000)
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="T", password="TestTest12",
                           captcha="1111"))
    # Error message for NickName field
    with pytest.allure.step("Error with incorrect nickname for nickname field"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][2]") == "Логин слишком короткий"
    # Border for nickname field
    with pytest.allure.step("Border for nickname field"):
        assert app.warning.get_border_color("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


@pytest.allure.step("Sign Up with space before nickname")
def test_sign_up_nick_space_before(app):
    random = randrange(1000000000)
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="testpm8+" + str(random) + "@gmail.com", username=" triced" + str(random),
                           password="TestTest12", captcha="1111"))
    # Error message for NickName field
    with pytest.allure.step("Error with incorrect nickname for nickname field"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][3]") == "Разрешены только a-z, 0-9 и _ символы"
    # Border for nickname field
    with pytest.allure.step("Border for nickname field"):
        assert app.warning.get_border_color("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


@pytest.allure.step("Sign Up with space as nickname")
def test_sign_up_nick_space_all(app):
    random = randrange(1000000000)
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="        " + str(random),
                           password="TestTest12", captcha="1111"))
    # Error message for NickName field
    with pytest.allure.step("Error with incorrect nickname for nickname field"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][3]") == "Разрешены только a-z, 0-9 и _ символы"
    # Border for nickname field
    with pytest.allure.step("Border for nickname field"):
        assert app.warning.get_border_color("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


@pytest.allure.step("Sign Up with empty password")
def test_sign_up_password_empty(app):
    random = randrange(1000000000)
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random), password="",
                           captcha="1111"))
    # Error message for password field
    with pytest.allure.step("Error with empty password for password field"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'password'][1]") == "Поле обязательно для заполнения"
    # Border for password field
    with pytest.allure.step("Border for password field"):
        assert app.warning.get_border_color(
            "//div[@id='registration']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"


@pytest.allure.step("Sign Up with empty email field")
def test_sign_up_empty_email(app):
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="", username="triced" + str(random), password="TestTest12", captcha="1111"))
        # Error message for email field
    with pytest.allure.step("Check empty email field error"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'email'][1]") == "Поле обязательно для заполнения"
    # Border for email field
    with pytest.allure.step("Border for email field"):
        assert app.warning.get_border_color("//input[@name='email']") == "rgba(187, 37, 37, 1)"


@pytest.allure.step("Sign Up with empty nickname field")
def test_sign_up_empty_nick(app):
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="", password="TestTest12",
                           captcha="1111"))
    # Error message for NickName field
    with pytest.allure.step("Check empty nickname field error"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'login'][1]") == "Поле обязательно для заполнения"
    # Border for nickname field
    with pytest.allure.step("Border for nickname field"):
        assert app.warning.get_border_color("//input[@name='nick']") == "rgba(187, 37, 37, 1)"


@pytest.allure.step("Sign Up with empty password field")
def test_sign_up_empty_password(app):
    with pytest.allure.step("If user is logged"):
        if app.session.user_logged():
            app.open_main_page_ru()
            app.session.logout()
        else:
            app.registration.sign_up(
                SignupCred(email="testpm8+" + str(random) + "@gmail.com", username="triced" + str(random), password="",
                           captcha="1111"))
    # Error message for password field
    with pytest.allure.step("Check empty password field error"):
        assert app.warning.get_outer_text(
            "//div[@id='registration']//span[@class='modala__error' and @data-validation-field = 'password'][1]") == "Поле обязательно для заполнения"
    # Border for password field
    with pytest.allure.step("Border for password field"):
        assert app.warning.get_border_color(
            "//div[@id='registration']//input[@name='password'][2]") == "rgba(187, 37, 37, 1)"

"""
