import pytest
from fixture.application import Application
fixture = None



@pytest.fixture(scope="session")
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None or fixture.isValide():
        fixture = Application(browser=browser)
    fixture.driver.fullscreen_window()
    request.addfinalizer(fixture.destroy)
    return fixture


@pytest.fixture(scope="session")
def app1(request):
    global fixture
    if fixture is None:
        fixture = Application(browser="chrome")
    else:
        if not fixture.isValide():
            fixture = Application(browser="chrome")
    request.addfinalizer(fixture.destroy)
    fixture.driver.fullscreen_window()
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--local", action="store", default="ru")




