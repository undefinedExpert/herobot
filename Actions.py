import re
from interactions.Clear_log import Clear_log

from Shared import Shared


class Actions(Shared):
    def __init__(self):
        super(Shared, self).__init__()

        self._clear_log = Clear_log()

    def clear_log(self):
        self._clear_log.run()

    def verify_endpoint(self, endpoint, err_msg='Failed to establish endpoint'):
        if self.endpoint == endpoint:
            return False
        else:
            self.log(err_msg + ' ' + endpoint)
            return True

    @staticmethod
    def get_sec(time):
        split_time = time.split(':')
        hours = int(split_time[0].replace('h', ''))
        minutes = int(split_time[1].replace('m', ''))
        seconds = int(split_time[2].replace('s', ''))

        return hours * 3600 + minutes * 60 + seconds

    def get_time_left(self, process_id):
        time_process_pattern = re.compile(r"Date\(\).getTime\(\)\+\d{0,4}\*\d{0,4}\)\;\$\('#" + process_id + "'\)", re.MULTILINE | re.DOTALL)
        time_pattern = re.compile(r"\d{0,4}\*\d{0,4}")

        script = self.browser.find('script', text=time_process_pattern)
        if script:
            matched_all = re.search(time_process_pattern, script.text)
            time = re.search(time_pattern, matched_all.group(0))

            if matched_all:
                time_left = time.group(0).split('*')[0]
                return int(time_left)


