from interactions.Clear_log import Clear_log


class Actions(Clear_log):
    def __init__(self):
        Clear_log.__init__(self)
        pass

    def clear_log(self):
        self.run()

    def verify_endpoint(self, endpoint, err_msg = 'Failed to establish endpoint'):
        if self.endpoint == endpoint:
            return True
        else:
            self.log(err_msg + ' ' + endpoint)
            return False
