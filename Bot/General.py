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
