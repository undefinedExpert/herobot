import re
from Bot.Shared import adapter


class CompleteTask:
    def __init__(self, task_desc='Edit log at localhost'):
        self.proc_length = 0
        self.which_task = task_desc
        self.process_id = None
        self.complete_route = '/processes?pid=%s' % self.process_id
        self.time = 0

        self.msgs = {
            'value': 'Process length is:',
            'task_desc_not_defined': 'You forget to define task_desc',
            'task_done': '%s has been completed' % self.which_task

        }
        # metody w tej klasie ignoruja ten dict
        # self.msg = {
        #     'proc_length': 'Process length is: %d ' % self.proc_length,
        #     'task_desc_not_defined': 'You forget to define task_desc',
        #     'task_done': '%s has been completed' % self.which_task,
        # }

    def run(self):
        # >go to task route
        adapter.browser.change_route('/processes?page=cpu')

        # >get list of processes,
        # TODO: it should all process not just list, select li
        process_list = adapter.window.find_all("ul", class_="list")

        # iterate over process list
        # adapter.log('length of process_list %s' % len(process_list))

        for process in process_list:
            self.complete_process(process)


    def complete_process(self, process):
        # get each process description
        description = process.select('.proc-desc')[0].text

        # if description match Edit log message
        if description == self.which_task:

            # then select process id
            self.process_id = process.select('.proc-desc')[0].parent.attrs['class'][1].replace('Block', '')
            # get time left from process
            self.time = self.get_time_left(self.process_id)

            # if process isn't completed yet
            self.wait_until_complete()

            # we move to appropriate endpoint with an id of our process, so we could finish this process
            # /processes?pid=32957978 complete endpoint
            complete_route = '/processes?pid=%s' % self.process_id.replace('process', '')
            adapter.browser.change_route(complete_route, silent=True)

            # FIXME: There is a problem with context of self in method log, tmp fix
            # task_done_msg = self.msg['task_done']
            adapter.log(self.msgs['task_done'])

    def wait_until_complete(self):
        while self.time > 0:
            adapter.log('task time left: %ss' % self.time, end='\r')
            # then we sleep this time
            self.time -= 1
            adapter.sleep_for(1)

    @staticmethod
    def get_sec(time):
        split_time = time.split(':')
        hours = int(split_time[0].replace('h', ''))
        minutes = int(split_time[1].replace('m', ''))
        seconds = int(split_time[2].replace('s', ''))

        return hours * 3600 + minutes * 60 + seconds

    @staticmethod
    def get_time_left(process_id):
        time_process_pattern = re.compile(r"Date\(\).getTime\(\)\+\d{0,4}\*\d{0,4}\)\;\$\('#" + process_id + "'\)",
                                          re.MULTILINE | re.DOTALL)
        time_pattern = re.compile(r"\d{0,4}\*\d{0,4}")

        script = adapter.window.find('script', text=time_process_pattern)
        if script:
            matched_all = re.search(time_process_pattern, script.text)
            time = re.search(time_pattern, matched_all.group(0))

            if matched_all:
                time_left = time.group(0).split('*')[0]
                return int(time_left)
