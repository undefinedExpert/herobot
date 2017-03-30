from Bot.Shared import adapter
from datetime import datetime, timezone
from Bot.interactions.CompleteTask import CompleteTask
import http.cookiejar
# Hack ip
# Connect IP
# Log Out Ip
# Save list of programs
# Save which ip program has connected

class Connection:
    def __init__(self, hack_method='bf'):
        # ip to hack from cookies
        self.method = 'bf'
        self.target = None

    def connect(self, target_ip, hack_method):
        # it log into appropriate ip
        # it should get user auth information
        # if no auth information
            # it should hack ip
                # if error occur it should save the ip with param well_protected
        # it should log into account using auth information

        if not target_ip:
            adapter.log('You should specify target ip')
            return False
        else:
            self.target = target_ip

        if hack_method:
            self.method = hack_method

        upcoming_route = "/internet?ip=%s" % self.target
        adapter.browser.change_route(upcoming_route, silent=False)

        # if ip not exist
        ip_not_exist = adapter.window.select('.widget-content.padding.noborder > a')[0].text
        if ip_not_exist == 'Back to First Whois':
            adapter.log('%s does not exist' % self.target)
            return False

        adapter.browser.change_route('/internet?action=login', silent=False)

        # check if user is already connected
        if len(adapter.window.select('#loginform')) <= 0:
            adapter.log('User already logged, please logout if you wish to get new connection')
            adapter.log('Moving to /internet?view=log')
            adapter.browser.change_route('/internet?view=log')
            return True

        auth_information = adapter.window.select('.form-actions > span')
        # handle bruteforce method
        if len(auth_information) <= 1:
            adapter.log('Wasnt found Username and password')
            adapter.log('Trying to hack %s' % self.target)

            if self.hack():
                complete_task = CompleteTask(task_desc='Crack server %s' % self.target)
                complete_task.run()
                auth_information = adapter.window.select('.form-actions > span')
            else:
                return False

        # login using user name and password
        adapter.browser.change_route('/internet?action=login', silent=False)
        username = auth_information[0].text.replace('Username: ', '')
        password = auth_information[1].text.replace('Password: ', '')
        adapter.log('Target username: %s, target password: %s' % (username, password))

        upcoming_route = '/internet?action=login&user=%s&pass=%s' % (username, password)
        adapter.browser.change_route(upcoming_route, silent=False)
        adapter.log('User has been logged to: %s successfully' % self.target)

        return True

    def disconnect(self):
        # logout route /internet?view=logout
        log_out_route = '/internet?view=logout'
        adapter.browser.change_route(log_out_route, silent=False)
        adapter.log('User has been logout from: %s successfully' % self.target)

    def hack(self):
        # try to hack
        adapter.browser.change_route('/internet?action=hack&method=bf')

        hack_failed = adapter.window.select('alert alert-error')
        browser = adapter.browser
        if len(hack_failed) > 0:
            adapter.log('Cannot hack %s' % self.target)
            return False

        return True
