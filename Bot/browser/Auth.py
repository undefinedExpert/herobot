from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests

class Auth:
    auth_fail = False
    driver = None

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
        self.session.get(self.full_url, headers=headers)
        self.session.cookies = self.cookies
        self.session.headers = headers

    def verify_auth(self):
        if self.window.url == self.full_url:
            self.log('Authorization successful')
            self.auth_fail = False
        else:
            self.log('failed to login')
            self.auth_fail = True
