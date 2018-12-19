import pytest


def test_get_users_id(app):
    app.admin.login_as_admin()
    app.admin.open_users_page()
    app.admin.get_user_for_month()
    app.admin.get_users_id()
