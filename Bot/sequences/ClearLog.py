from Bot.interactions.GetLogForm import GetLogForm
from Bot.interactions.CompleteTask import CompleteTask


class ClearLog(GetLogForm, CompleteTask):
    route_required = '/log'

    def __init__(self):
        super().__init__()

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
        self.change_form()

        # >go to task route
        self.change_route('/processes?page=cpu')

        # >Complete task
        self.complete_task()
