class GetLogForm:
    def change_form(self):
        form = self.__get_form()
        log_area = form['log']

        if log_area.value == 'test':
            self.log('Log is already removed')
            return

        log_area.value = 'test'
        self.browser.submit_form(form)

    def __get_form(self):
        return self.browser.get_form(action='logEdit')