from robobrowser import RoboBrowser
from Bot.Shared import Shared


class Browser(Shared):
    def __init__(self):
        super().__init__()

    def change_route(self, end_point):
        self.set_url_endpoint(end_point)
        self.build_url()
        self.open()
        self.log_urls()

    def open(self):
        self.browser.open(self.full_url)

    def build_url(self):
        self.full_url = self.url + self.endpoint

    def set_url_endpoint(self, next_endpoint):
        self.endpoint = next_endpoint
        self.build_url()

    def log_urls(self, custom=None):
        print('\n------ URLS STATUS -------')
        print('Current url: %s' % self.browser.url)
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
        self.browser = RoboBrowser(history=True, parser='html.parser', session=self.session)

        self.browser.open(self.full_url, cookies=self.cookies)
