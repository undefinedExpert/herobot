from Bot.Shared import adapter

from Bot.db.Database import connect
from Bot.db.create_server_information import *

class ServerAnalyse:
    # verify the route, it should be internet?view=software
    # gathering server information:
        # checking the hdd size
        # check the internet connection
        # software installed
        # available software
    # save the information in database

    # open route
    # Select hdd size
        # push the size into server_information dict
        # push the available size into server_information dict
    # Select internet connection
        # push the speed of it into server_information dict
    # Get all software names
        # if software is running, mark as 'installed'
        # get each software and push into array, inside of our server_information
    # return server_information



    def __init__(self, target):
        self.target = target


    def analyse(self):
        # change route
        adapter.browser.change_route(end_point='/internet?view=software', silent=False)

        hdd = self.get_hdd()
        adapter.log(hdd)
        network = self.get_internet_connection()
        software = self.get_software_names()

        adapter.log('Server information collected')
        collected = {"hdd": hdd, "network": network, "software": software}

        # save in database
        self.save_server_information(collected)

        return collected


    def get_hdd(self):
        # hd-usage.green for whole dick space
        # hd-usage.red free space
        hd_usage = adapter.window.find('div', class_='hd-usage')
        spaces = hd_usage.find('span', class_='small').text.split('/')

        stripped = []
        for space in spaces:
            whitespace_removed = space.replace(' ', '')
            stripped.append(whitespace_removed)

        hd_space = stripped[1]
        hd_taken = stripped[0]
        hd_free = self.calc_hdd_taken(hd_space, hd_taken)

        return {'all': hd_space, 'free': hd_free, 'taken': hd_taken}

    @staticmethod
    def get_internet_connection():
        software = adapter.window.find('div', id='softwarebar')
        network = software.select('span.small strong')[0].text

        return network


    def get_software_names(self):
        # TODO: Get all the list of software
        # TODO: Mark software if they are installed on mine
        # TODO: Return a list of consist software list, each with version, name, size, type (e.g spam virus)
        all_soft = []
        # schema = {
        #     "name": '',
        #     "version": 1.0,
        #     "type": '',
        #     "extension": '',
        #     "size": '150MB',
        #     "marks": {
        #         'installed': False,
        #         'hidden': False,
        #         'my_own': False,
        #     },
        #     'software_id': 0
        # }
        # handle exception when there is no softs

        software = adapter.window.select('.table-software tbody tr')
        for soft in software:
            # <i> installed by me
            cls = soft.attrs['class']
            id = soft.attrs['id']
            installed = False
            my_own = False
            app_name = ''
            app_type = ''
            app_version = ''
            app_size = ''

            app_ingame_id = id

            if 'installed' in cls:
                installed = True

            content = soft.contents

            # find type
            if content[1].find('span') is not None:
                app_type = content[1].find('span').attrs['title']

            # find name
            if content[3].find('b') is not None:
                test = content[3].find('b')
                app_name = content[3].find('b').text

            elif content[3].find('i') is not None:
                app_name = content[3].find('i').text
                my_own = True

            elif content[3].text:
                app_name = content[3].text.replace('\n', '')

            # find version
            if content[5].find('font') is not None:
                app_version = content[5].find('font').text

            # find size
            if content[7].find('font') is not None:
                app_size = content[7].find('font').text

            all_soft.append({
                "name": app_name,
                "type": app_type,
                "version": app_version,
                "size": app_size,
                "installed": installed,
                "my_own": my_own,
                "game_id": app_ingame_id,
            })

        return all_soft


    def save_server_information(self, collected):
        adapter.log('Adding server into database')
        insert_server(self.target)

        adapter.log('Server information saved in database')
        for app in collected['software']:
            add_app(app, self.target)

        add_hardware(collected['hdd'], collected['network'], self.target)


    def filter_new_lines(self, array):
        temp = []
        for item in array:
            if '\n' in item:
                continue
            else:
                temp.append(item)

        return temp

    def calc_hdd_taken(self, all, taken):
        # check if mb or gb
        # if all contains gb multiply by 1000
        # if all contains tb multiply by 1000000
        # calc difference between all and taken, receive result in mb
        # divide mb on gb
        # if greater then 1000, divide by another 1000 and add tb
        all_space_mb = self.get_mb_int(all)
        taken_space = self.get_mb_int(taken)

        difference = self.convert_to_highest(all_space_mb - taken_space)

        return difference

    @staticmethod
    def get_mb_int(value):
        result = 0

        if 'MB' in value:
            result = int(value.replace('MB', ''))

        if 'GB' in value:
            result = int(value.replace('GB', '')) * 1000

        if 'TB' in value:
            result = int(value.replace('TB', '')) * 1000000

        return result

    @staticmethod
    def convert_to_highest(value):
        result = ''

        if value >= 1000000:
            result = str(value / 1000000) + 'TB'

        elif value >= 1000:
            result = str(value / 1000) + 'GB'

        else:
            result = str(value) + 'MB'

        return result







