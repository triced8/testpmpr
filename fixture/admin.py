class AdminHelper:

    def __init__(self, app):
        self.app = app

    def open(self):
        driver = self.app.driver
        driver.get("https://beta.pokermatch.com/sa")