import pytest
import time
from model.credLogin import Group
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture =Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login(app):
   app.session.login(Group(username="triced", password="TestTest12"))
   app.session.logOut()

def test_signUp(app):
    app.signUp()


def test_openadmin(app):
    app.session.login(Group(username="tricedu", password="TestTest12"))
    time.sleep(0.1)
    app.session.opensa()

