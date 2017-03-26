from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import requests

from Config import Config


class Auth(object):
    def __init__(self):
        self.cookies = None
        self.auth_fail = False
        self.driver = None

    def request_login(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

        delay = 120  # seconds
        try:
            element = WebDriverWait(self.driver, delay).until(
                EC.presence_of_element_located((By.ID, "sidebar"))
            )
        finally:
            self.log('User has logged')
            self.save_cookies()
            self.driver.quit()

    def configure_session(self):
        load_cookies = self.load_cookies()

        if load_cookies and not self.cookies and not self.auth_fail:
            self.log('Restoring cookies')
            self.cookies = load_cookies
        else:
            self.request_login()
            self.cookies = self.load_cookies()

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

        self.session = requests.Session()
        self.session.get(self.fullUrl, headers=headers)
        self.session.cookies = self.cookies
        self.session.headers = headers

    def save_cookies(self):
        temp_cookies = {}
        for s_cookie in self.driver.get_cookies():
            temp_cookies[s_cookie["name"]] = s_cookie["value"]

        try:
            with open('s.json', 'w') as outfile:
                json.dump(temp_cookies, outfile)
        except IOError:
            self.log('s.json does not exist')

    def load_cookies(self):
        try:
            with open('s.json', encoding='utf-8') as data_file:
                self.log('Loading cookies')

                try:
                    data = json.loads(data_file.read())
                    cookies_jar = requests.utils.cookiejar_from_dict(data)
                    return cookies_jar
                except ValueError:
                    self.log('No previous session found')
                    return False

        except IOError:
            self.log('There is no previous cookies')
            return False

    def verify_auth(self):
        if self.browser.url == self.fullUrl:
            self.log('Authorization successful')
            self.auth_fail = False
        else:
            self.log('failed to login')
            self.auth_fail = True

    def auth(self):
        # login
        pass
