from Auth import Auth
from Browser import Browser
from Actions import Actions

from Shared import Shared

class Bot(Browser, Actions):
    def __init__(self, url, endpoint):
        Shared.url = url
        Shared.endpoint = endpoint

        Browser.__init__(self)
        Actions.__init__(self)

        self.auth = Auth()

    def start(self):
        self.auth.configure_session()
        self.create_connection()
        self.auth.verify_auth()
        self.log_urls()

