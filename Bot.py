from time import sleep

from Config import Config
from Auth import Auth
from Browser import Browser
from Actions import Actions


class Bot(Auth, Config, Browser, Actions):
    def __init__(self, url, endpoint):
        Config.__init__(self, url, endpoint)
        Auth.__init__(self)
        Browser.__init__(self)
        Actions.__init__(self)

    def start(self):
        self.configure_session()
        self.create_connection()
        self.verify_auth()
        self.log_urls()

    @staticmethod
    def log(msg):
        print('LOG MESSAGE: %s' % msg)


    @staticmethod
    def sleep_for(time):
        sleep(time)
