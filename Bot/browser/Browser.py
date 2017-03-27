from robobrowser import RoboBrowser

from Bot.browser.Auth import Auth


class Browser(Auth):
    def __init__(self, url, full_url, endpoint, log):
        self.window = None
        self.url = url
        self.full_url = full_url
        self.endpoint = endpoint
        self.session = None
        self.cookies = None
        self.log = log

        super().__init__()

    def change_route(self, end_point, silent=False):
        self.set_url_endpoint(end_point)
        self.build_url()
        self.window.open(self.full_url)
        self.log_urls(silent)

    def build_url(self):
        self.full_url = self.url + self.endpoint

    def set_url_endpoint(self, next_endpoint):
        self.endpoint = next_endpoint
        self.build_url()

    def log_urls(self, custom=None, silent=False):
        if silent is not False:
            print('\n------ URLS STATUS -------')
            print('Current url: %s' % self.window.url)
            print('Full url: %s' % self.full_url)
            print('Endpoint url: %s' % self.endpoint)

            if custom:
                print('Next url: %s' % custom)

            print('---------- END -----------\n')

    def create_connection(self):
        if not self.session or not self.cookies:
            self.log('Could not establish session, or cookies.')
            return

        self.log('Creating connection')
        self.window = RoboBrowser(history=True, parser='html.parser', session=self.session)

        self.window.open(self.full_url, cookies=self.cookies)
