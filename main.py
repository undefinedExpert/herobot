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
        'reauth',
        'open',
        'log_urls',
        '/next_endpoint',
        'end'
    ]
    print('\nRun one of following commands:')
    for index, command in enumerate(commands):
        print('%s. %s' % (str(index), command))

    answer = input('Run: ')

    if answer == 'clear_log':
        bot.clear_log()

    elif answer == 'open':
        bot.open()

    elif answer[0] == '/':
        bot.set_url_endpoint(answer)

    elif answer == 'load_cookies':
        bot.load_cookies()

    elif answer == 'reauth':
        bot.start()

    elif answer == 'log_urls':
        bot.log_urls()

    elif answer == 'end':
        isEnd = True

