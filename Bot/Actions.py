from Bot.sequences.ClearLog import ClearLog
from Bot.sequences.InvadeIp import InvadeIp


class Actions:
    def __init__(self):
        self._clear_log = ClearLog()
        self._invade_ip = InvadeIp()

    def clear_log(self):
        self._clear_log.run()

    def invade_ip(self):
        self._invade_ip.run()
