import time
import pytest
from model.credLogin import LoginCred

@pytest.allure.step("Open slot page for non-Auth user")
def test_slot_button(app):
    with pytest.allure.step("Open slots page"):
        app.pages.open_slots_page()


@pytest.allure.step("Open slot page for Auth user")
def test_open_slot_page(app):
    with pytest.allure.step("Open main page"):
        app.open_main_page_ru()
    with pytest.allure.step("Login to triced user"):
        app.session.login(LoginCred(username="triced", password="TestTest12"))
    with pytest.allure.step("Open slots page"):
        app.pages.open_slots_page()