from Bot import Bot

mainUrl = 'https://legacy.hackerexperience.com'
mainEndpoint = '/log'

bot = Bot(mainUrl, mainEndpoint)
bot.start()

# TODO: clean_log should also accept button
# TODO: Work on a project structure, class hierarchy, class inheritance
# TODO: Fix problem with extracing cookies from session where user didn't have any cookies at all, or they changed
#       AttributeError: 'dict' object has no attribute 'extract_cookies'
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

