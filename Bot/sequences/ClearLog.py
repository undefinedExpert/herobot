from Bot.Shared import adapter
from Bot.interactions.GetLogForm import GetLogForm
from Bot.interactions.CompleteTask import CompleteTask

# ta klasa powinna miec dostep do czego?
# do shared
# oraz powinna tworzyc insancje swoich interackji


class ClearLog:
    route_required = '/log'

    def __init__(self):
        self.log_form = GetLogForm()
        self.complete_task = CompleteTask()

    '''
        - It changes route to /log
        - It changes the log textarea to eql 'test'
        - it submits form and confirms when
    '''

    def run(self):
        # >verify endpoint
        if adapter.verify_endpoint(self.route_required):
            adapter.log('moving to %s' % self.route_required)
            adapter.browser.change_route(self.route_required)
        else:
            adapter.log('refreshing %s' % self.route_required)
            adapter.browser.change_route(self.route_required)

        # >get form
        # >fill the form
        # >send the form
        self.log_form.run()

        # >go to task route
        adapter.browser.change_route('/processes?page=cpu')

        # >Complete task
        self.complete_task.run()


