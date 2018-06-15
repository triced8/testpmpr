import pytest
from model.credLogin import Group
from fixture.application import Application
import time

@pytest.fixture()
def app(request):
    fixture =Application()
    request.addfinalizer(fixture.destroy)
    return fixture


#def test_login(app):
#   app.login(Group(username="triced", password="TestTest12"))
#    app.logOut()

#def test_signUp(app):
#    app.signUp()


def test_openadmin(app):
    app.login(Group(username="tricedu", password="TestTest12"))
    time.sleep(0.1)
    app.opensa()

