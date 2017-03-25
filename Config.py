class Config(object):
    def __init__(self, url, endpoint):
        self.url = url
        self.endpoint = endpoint
        self.fullUrl = self.url + self.endpoint
        self.browser = None
        self.session = None
        self.cookies = None

