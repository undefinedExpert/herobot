from time import sleep
from Bot.browser.Browser import Browser


# TODO: Remove Methods and make this class Abstract
class Shared:
    def __init__(self):
        self.url = 'https://legacy.hackerexperience.com'
        self.endpoint = '/log'
        self.full_url = self.url + self.endpoint
        self.session = None
        self.cookies = None
        self.window = None

        self.browser = Browser(log=self.log, url=self.url, full_url=self.full_url, endpoint=self.endpoint)

    @staticmethod
    def log(msg, **kwargs):
        print('LOG MESSAGE: %s' % msg, **kwargs)

    @staticmethod
    def sleep_for(time):
        sleep(time)

    def verify_endpoint(self, endpoint, err_msg='Failed to establish endpoint'):
        if self.endpoint == endpoint:
            return False
        else:
            self.log(err_msg + ' ' + endpoint)
            return True


# TODO: Rename to WebAdapter
class AdapterShared:
    def __init__(self):
        self.shared = Shared()
        self.browser = self.shared.browser

    @property
    def window(self):
        return self.browser.window

    def verify_endpoint(self, *args):
        return self.shared.verify_endpoint(*args)

    def sleep_for(self, *args):
        return self.shared.sleep_for(*args)

    def log(self, msg, **kwargs):
        return self.shared.log(msg, **kwargs)

adapter = AdapterShared()
