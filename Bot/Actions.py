from Bot.sequences.ClearLog import ClearLog


class Actions:
    def __init__(self):
        self._clear_log = ClearLog()

    def clear_log(self):
        self._clear_log.run()
