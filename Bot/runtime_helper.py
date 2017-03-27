# import json
# #
# # temp_cookies = {'value': 'leszczyku'}
# #
# # try:
# #     with open('tmp/cookies.json', 'w+') as outfile:
# #         json.dump(temp_cookies, outfile)
# # except IOError:
# #     print('problem')
#
# import os
# from Bot.definitions import ROOT_DIR, CONFIG_PATH, TEMP_PATH
#
# temp_cookies = {'value': 'leszczyku'}
# #
# filepath = os.path.join(TEMP_PATH, 'cookies.json')
# if not os.path.exists(TEMP_PATH):
#     os.makedirs(TEMP_PATH)
#
#
# print(filepath)
# with open(filepath, 'w+') as outfile:
#     json.dump(temp_cookies, outfile)
