import pytest
from fixture.application import Application
fixture = None




@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.driver.fullscreen_window()
    else:
        if not fixture.isValide():
            fixture = Application()
            fixture.driver.fullscreen_window()
    request.addfinalizer(fixture.destroy)
    return fixture


