from Bot.Actions import Actions
from Bot.Shared import adapter


class Bot(Actions):
    def __init__(self):
        self.shared = adapter.shared
        self.browser = adapter.browser
        self.window = None
        super().__init__()

    def start(self):
        self.browser.configure_session()
        self.browser.create_connection()
        self.browser.verify_auth()
        self.browser.log_urls()

    def log_urls(self):
        self.browser.log_urls(silent=False)

    def change_route(self, route, silent):
        self.browser.change_route(route, silent=silent)

    def save_cookies(self):
        self.browser.save_cookies(cookies=True)

    def display_cookies(self):
        print(self.browser.session.cookies)
        print(self.browser.session.cookies.get('ip-data'))

