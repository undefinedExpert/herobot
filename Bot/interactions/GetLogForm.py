from Bot.Shared import adapter


class GetLogForm:
    def __init__(self, value='I see you :)'):
        super().__init__()
        self.which_form = 'logEdit'
        self.value = value

    def run(self):
        try:
            form = self.__get_form()
            log_area = form['log']
        except TypeError:
            adapter.log('Log form wasn\'t found')
            return False

        if log_area.value == self.value:
            adapter.log('Log already removed')
            return False

        log_area.value = self.value
        adapter.window.submit_form(form)

        return True

    def __get_form(self):
        return adapter.window.get_form(action=self.which_form)
