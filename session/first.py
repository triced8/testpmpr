import pytest
from .credLogin import Group
from .application import Application



@pytest.fixture()
def app(request):
    fixture =Application()
    return fixture
    request.addfinalizer(fixture.destroy)

def test_login(app):
    app.login(Group(username="triced", password="TestTest12"))
    app.logOut()

def test_signUp(app):
    app.ssignUp()


if __name__ == "__main__":
    unittest.main()
