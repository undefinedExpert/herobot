from robobrowser import RoboBrowser


class Browser(object):
    def __init__(self):
        self.browser = None
        self.session = None
        self.cookies = None

    def change_route(self, end_point):
        self.set_url_endpoint(end_point)
        self.build_url()
        self.open()

    def open(self):
        self.browser.open(self.fullUrl)

    def build_url(self):
        self.fullUrl = self.url + self.endpoint

    def set_url_endpoint(self, next_endpoint):
        self.endpoint = next_endpoint
        self.build_url()
        self.log_urls()

    def log_urls(self, custom=None):
        print('\n------ URLS STATUS -------')
        print('Current url: %s' % self.browser.url)
        print('Full url: %s' % self.fullUrl)
        print('Endpoint url: %s' % self.endpoint)

        if custom:
            print('Next url: %s' % custom)

        print('---------- END -----------\n')

    def create_connection(self):
        self.log('Creating connection')
        self.browser = RoboBrowser(history=True, parser='html.parser', session=self.session)
        self.browser.open(self.fullUrl, cookies=self.cookies)