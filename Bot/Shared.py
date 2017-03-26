from time import sleep


class Shared:
    url = 'https://legacy.hackerexperience.com'
    endpoint = '/log'
    full_url = url + endpoint
    browser = None
    session = None
    cookies = None

    @staticmethod
    def log(msg):
        print('LOG MESSAGE: %s' % msg)

    @staticmethod
    def sleep_for(time):
        sleep(time)
