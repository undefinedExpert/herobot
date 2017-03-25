class Clear_log(object):
    def __init__(self):
        self.endpoint = '/log'

    def run(self):
        self.verify_endpoint(self.endpoint)

        form = self.browser.get_form(action='logEdit')
        log_area = form['log']
        log_area.value = 'test'

        self.browser.submit_form(form)
        self.log('log has been changed to %s' % log_area.value)

        self.log('moving to task manager and accepting button')
        self.change_route('/processes?page=cpu')

        process_list = self.browser.find_all("ul", class_="list")

        print('length of process_list %s' % len(process_list))
        for process in process_list:
            description = process.select('.proc-desc')[0].text

            if description == 'Edit log at localhost':
                self.log('znalazlem description edit log!!')
                # TODO: Zrobic by to dzialalo!!! narazie nie dziala xD
                # complete_form = process.get_form(method_='GET')
                # self.browser.submit_form(complete_form)
                # teraz powinnienem kliknac w tym procesie
                # button!!

        self.log('sleep for 10 seconds')
        self.sleep_for(10)

        self.log('moving to software page')
        self.open()
