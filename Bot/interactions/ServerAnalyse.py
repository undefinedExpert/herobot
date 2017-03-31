from Bot.Shared import adapter


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



    def __init__(self):
        pass

    def analyse(self):
        # change route
        adapter.browser.change_route(end_point='/internet?view=software', silent=False)

        hdd = self.get_hdd()
        adapter.log(hdd)
        network = self.get_internet_connection()
        # software = self.get_software_names()
        print('%s space and free is %s, with network connection of %s' % (hdd['all'], hdd['free'], network))


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
        hd_free = stripped[0]

        return {'all': hd_space, 'free': hd_free}

    def get_internet_connection(self):
        software = adapter.window.find('div', id='softwarebar')
        network = software.select('span.small strong')[0].text

        return network


    def get_software_names(self):
        pass

    def save_server_information(self):
        pass




