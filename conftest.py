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
    fixture.driver.fullscreen_window()
    return fixture


@pytest.fixture(scope="session")
def app1(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.isValide():
            fixture = Application()
    request.addfinalizer(fixture.destroy)
    fixture.driver.fullscreen_window()
    return fixture
