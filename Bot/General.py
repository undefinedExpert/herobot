from Bot.Auth import Auth
from Bot.Browser import Browser
from Bot.Actions import Actions
from Bot.Shared import Shared


class Bot(Auth, Browser, Shared, Actions):
    def __init__(self):
        super().__init__()

        print('Bot MRO')
        print(Bot.__mro__)

    def start(self):
        self.configure_session()
        self.create_connection()
        self.verify_auth()
        self.log_urls()

