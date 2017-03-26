from time import sleep


class Shared_Blueprint:
    def __init__(self):
        self.url = ''
        self.endpoint = ''
        self.fullUrl = self.url + self.endpoint
        self.browser = None
        self.session = None
        self.cookies = None

    @staticmethod
    def log(msg):
        print('LOG MESSAGE: %s' % msg)

    @staticmethod
    def sleep_for(time):
        sleep(time)

    @property
    def url(self):
        return self.url

    @url.setter
    def url(self, value):
        self.url = value

    @property
    def endpoint(self):
        return self.endpoint

    @endpoint.setter
    def endpoint(self, value):
        self.url = value

    @property
    def browser(self):
        return self.browser

    @browser.setter
    def browser(self, value):
        self.browser = value

    @property
    def session(self):
        return self.session

    @session.setter
    def session(self, value):
        self.session = value

    @property
    def cookies(self):
        return self.cookies

    @cookies.setter
    def cookies(self, value):
        self.cookies = value


Shared = Shared_Blueprint()
