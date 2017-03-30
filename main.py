from Bot.General import Bot

bot = Bot()
bot.start()

# TODO: Usuwanie loga podczas gdy istnieja inne procesy (wiecej niz 1)
# Sledzenie aktywnosci na logu i zapisywanie do bazy danych informacje o tym kto sie zalogwal kiedy i kim jest
# Chodzenie po ip, rozsylanie wirusa, zbieranie informacji na temat softu, systemu.
# zmiana ip

isEnd = False
while not isEnd:
    commands = [
        'clear_log',
        'invade_ip',
        '/next_endpoint',
        'reauth',
        'log_urls',
        'end'
    ]
    print('\nRun one of following commands:')
    for index, command in enumerate(commands):
        print('%s. %s' % (str(index), command))

    answer = input('Run: ')

    if answer == '0':
        bot.clear_log()

    elif answer == '1':
        bot.invade_ip()

    elif answer[0] == '/':
        bot.change_route(answer, silent=False)

    elif answer == '2':
        bot.start()

    elif answer == '3':
        bot.log_urls()

    elif answer == 'save_cookies':
        bot.save_cookies()

    elif answer == 'disconnect':
        bot.disconnect_ip()

    elif answer == 'display_cookies':
        bot.display_cookies()

    elif answer == '4':
        isEnd = True


