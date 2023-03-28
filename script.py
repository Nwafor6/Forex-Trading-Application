# import MetaTrader5 as mt5

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trading.settings")

# import django
# django.setup()

# from django.core.management import call_command

# # display data on the MetaTrader 5 package
# # print("MetaTrader5 package author: ",mt5.__author__)
# # print("MetaTrader5 package version: ",mt5.__version__)

# # Import the account credentials from settings
# from django.conf import settings
# # account=
# # for account, server, password in settings.ACCOUNT_NUMBERS, settings.SERVERS, settings.PASSWORDS:
# ACCOUNT_NUMBERS=[22014542, 51135132, 51135134]
# SERVERS=["Deriv-Demo","ICMarketsEU-Demo","ICMarketsEU-Demo"]
# PASSWORDS=["duzftxd8","yym2fmut","u5qoleim"]
# for i in range(3):
#     print(ACCOUNT_NUMBERS[i], SERVERS[i],PASSWORDS[i])

#     if not mt5.initialize(login=ACCOUNT_NUMBERS[i], server=SERVERS[i], password=PASSWORDS[i]):
#         print("initialize() failed, error code =",mt5.last_error())
#         quit()
#     account=mt5.account_info()
#     balance=account.balance
#     equity=account.equity
#     print(balance, equity)
# mt5.shutdown()


import time
def fetch_data():
    print("Hello background")
    return "Hello world"

def main():
    while True:
        data = fetch_data()
        print(data)
        # time.sleep(60)
