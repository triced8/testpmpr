import pytest
from fixture.application import Application

fixture = None


@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.isValide():
            fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

"""
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensureLogout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
"""