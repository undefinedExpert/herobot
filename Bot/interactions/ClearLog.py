class ClearLog:
    def __init__(self):
        super().__init__()
        print('ClearLog mro')
        print(ClearLog.__mro__)
        self.route_required = '/log'

    '''
        - It changes route to /log
        - It changes the log textarea to eql 'test'
        - it submits form and confirms when
    '''

    def run_clear_log(self):
        self.__run()

    def __run(self):
        # >verify endpoint
        if self.verify_endpoint(self.route_required):
            self.log('moving to %s' % self.route_required)
            self.change_route('/log')
        else:
            self.log('refreshing %s' % self.route_required)
            self.change_route('/log')

        # >get form
        # >fill the form
        # >send the form
        form = self.__get_form()
        log_area = form['log']

        if log_area.value == 'test':
            self.log('Log is already removed')
            return

        log_area.value = 'test'
        self.browser.submit_form(form)

        # >go to task route
        self.change_route('/processes?page=cpu')

        # >get list of processes
        process_list = self.browser.find_all("ul", class_="list")

        # iterate over process list
        print('length of process_list %s' % len(process_list))
        for process in process_list:
            # get each process description
            description = process.select('.proc-desc')[0].text

            # if description match Edit log message
            if description == 'Edit log at localhost':

                # then select process id
                process_id = process.select('.proc-desc')[0].parent.attrs['class'][1].replace('Block', '')

                # get time left from process
                time = self.get_time_left(process_id)

                # if process isn't completed yet
                if time > 0:
                    self.log('task time left: %ss' % time)
                    self.log('sleeping for: %ss' % time)
                    # then we sleep this time
                    self.sleep_for(time)

                # we move to appropriate endpoint with an id of our process, so we could finish this process
                # /processes?pid=32957978 complete endpoint
                complete_route = '/processes?pid=%s' % process_id.replace('process', '')
                self.change_route(complete_route)

                self.log('Log cleaning completed')

    def __get_form(self):
        return self.browser.get_form(action='logEdit')
