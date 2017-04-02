from Bot.Shared import adapter
from Bot.interactions.Connection import Connection
from Bot.interactions.GetLogForm import GetLogForm
from Bot.interactions.CompleteTask import CompleteTask
from Bot.interactions.ServerAnalyse import ServerAnalyse

class InvadeIp:
    target_ip = '241.151.9.102'
    # target_ip = '206.128.223.106'
    hack_method = 'bf'
    route_required = '/internet'

    def __init__(self):
        # self.log_form = GetLogForm()
        self.connection = Connection()
        self.log_form = GetLogForm(value='kutasiarze, chuj w dupsko')
        self.server_analyse = ServerAnalyse(target=self.target_ip)

        task_desc = 'Edit log at %s' % self.target_ip
        self.complete_task = CompleteTask(task_desc=task_desc)

    def run(self):
        adapter.log(self.target_ip)
        # >verify endpoint
        if adapter.verify_endpoint(self.route_required):
            adapter.log('moving to %s' % self.route_required)
            adapter.browser.change_route(self.route_required, silent=True)
        else:
            adapter.log('refreshing %s' % self.route_required)
            adapter.browser.change_route(self.route_required, silent=True)

        # connect with ip
        connected = self.connection.connect(target_ip=self.target_ip, hack_method=self.hack_method)
        if not connected:
            adapter.log('Couldn\'t log into %s' % self.target_ip)
            return False

        # self.clear_enemy_log()

        self.server_analyse.analyse()

        adapter.log('disconnecting from server %s ' % self.target_ip)
        self.disconnect()
        # check enemy machine (network speed, disk space, apps installed)
        # save collected data
        # upload software,
        # wait until uploaded software done
        # run this software
        # remove only those information which contian my ip

    def disconnect(self):
        self.connection.disconnect()

    def clear_enemy_log(self):
        # TODO: Analyse enemy log, check if he might be online
        # if he does not seem to be online, upload virus
        # else check software and log later
        # Also we should only delete our ip from log, just entire log

        self.log_form.run()

        # >go to task route
        adapter.browser.change_route('/processes?page=cpu')

        # >Complete task
        self.complete_task.run()

        adapter.browser.change_route('/internet?view=logs', silent=True)
        adapter.log('Moving to enemy log route')

