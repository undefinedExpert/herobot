from robobrowser import RoboBrowser
import json
import os
import requests
from Bot.browser.Auth import Auth
from Bot.definitions import TEMP_PATH
import urllib

class Browser(Auth):
    def __init__(self, url, full_url, endpoint, log):
        self.cookies_path = os.path.join(TEMP_PATH, 'cookies.json')
        self.window = None
        self.url = url
        self.full_url = full_url
        self.endpoint = endpoint
        self.session = None
        self.cookies = None
        self.log = log

        super().__init__()

    def change_route(self, end_point, silent=True):
        self.set_url_endpoint(end_point)
        self.build_url()
        self.window.open(self.full_url)
        self.log_urls(silent=silent)

    def build_url(self):
        self.full_url = self.url + self.endpoint

    def set_url_endpoint(self, next_endpoint):
        self.endpoint = next_endpoint
        self.build_url()

    def log_urls(self, custom=None, silent=True):
        if not silent:
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

    def get_json_cookies(self, cookies):
        temp_cookies = {}
        cookies = cookies

        for s_cookie in cookies:
            temp_cookies[s_cookie["name"]] = s_cookie["value"]

        return temp_cookies

    def get_cookie_jar(self, cookies_json):
        cookies_jar = requests.utils.cookiejar_from_dict(cookies_json)
        return cookies_jar

    def save_cookies(self, cookies=False):
        temp_cookies = self.get_json_cookies(self.driver.get_cookies())

        try:

            if not os.path.exists(TEMP_PATH):
                os.makedirs(TEMP_PATH)

            with open(self.cookies_path, 'w+') as outfile:
                json.dump(temp_cookies, outfile)

        except IOError:
            self.log('Unexpected error appear while reading cookies file')

    def load_cookies(self):
        try:
            with open(self.cookies_path, encoding='utf-8') as data_file:
                try:
                    data = json.loads(data_file.read())
                    cookies_jar = self.get_cookie_jar(data)
                    self.log('Cookies restored')
                    return cookies_jar
                except ValueError:
                    self.log('No previous session found')
                    return False

        except IOError:
            self.log('There is no previous cookies')
            return False

    def modify_cookie(self, name, value):
        try:
            with open(self.cookies_path, encoding='utf-8') as data_file:
                try:
                    data = json.loads(data_file.read())

                    self.log('Changed cookie %s to %s' % (name, value))
                    data[name] = value

                    cookies_jar = requests.utils.cookiejar_from_dict(data)
                    self.window.session.cookies = cookies_jar
                except ValueError:
                    self.log('No cookies found')
                    return False

        except IOError:
            self.log('There is no previous cookies')
            return False

    def decode_cookie(self, cookie):
        return urllib.parse.unquote_plus(cookie)


    def encode_cookie(self, cookie):
        return urllib.parse.quote_plus(cookie, encoding='utf-8').replace('%25', '%')

    def get_cookie(self, name):
        cookies = self.window.session.cookies
        return cookies.get(name)

    def set_cookie(self, name, value, domain):
        cookies = self.window.session.cookies
        return cookies.set(name, value, domain)
