from time import sleep


class Shared:
    url = None
    endpoint = None
    full_url = None
    browser = None

    def __init__(self):
        self.session = None
        self.cookies = None

    @staticmethod
    def log(msg):
        print('LOG MESSAGE: %s' % msg)

    @staticmethod
    def sleep_for(time):
        sleep(time)
