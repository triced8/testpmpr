import time
from model.credLogin import LoginCred






def test_login(app):
    app.session.login(LoginCred(username="triced", password="TestTest12"))
    app.session.logout()
    time.sleep(0.1)

"""
def test_openadmin(app):
    app.session.login(Group(username="tricedu", password="TestTest12"))
    time.sleep(0.1)
    app.admin.open()


def test_emptyLogin(app):
    app.session.login(Group(username="", password=""))
    app.session.logout()
"""