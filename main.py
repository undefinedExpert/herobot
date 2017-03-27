from Bot.General import Bot

bot = Bot()
bot.start()

# TODO: Usuwanie loga podczas gdy istnieja inne procesy (wiecej niz 1)
isEnd = False
while not isEnd:
    commands = [
        'clear_log',
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

    elif answer[0] == '/':
        bot.change_route(answer)

    elif answer == '2':
        bot.start()

    elif answer == '3':
        bot.log_urls()

    elif answer == '4':
        isEnd = True

