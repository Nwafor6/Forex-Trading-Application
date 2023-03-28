import json
from bson import Decimal128
import asyncio
import threading
import time
from django.conf import settings
import MetaTrader5 as mt5
from .models import Account
from datetime import datetime
import datetime

import pymongo
from datetime import datetime, timedelta
import pymt5

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(fetch_and_save_data())

def fetch_and_save_data():
    while True:
         
            # Connect to MongoDB database
        client = pymongo.MongoClient(settings.MONGO_DB)
        db = client["las4zan"]
        accounts_col = db["accounts"]

        # Define account details
        ACCOUNT_NUMBERS=[22014542, 51135132, 51135134]
        SERVERS=["Deriv-Demo","ICMarketsEU-Demo","ICMarketsEU-Demo"]
        PASSWORDS=[settings.PASSWORD1,settings.PASSWORD2,settings.PASSWORD3]

        # Connect to each account and save data at 1-minute intervals
        for i in range(3):
            if not mt5.initialize(login=ACCOUNT_NUMBERS[i], server=SERVERS[i], password=PASSWORDS[i]):
                print("initialize() failed, error code =", pymt5.last_error())
                quit()

            account = mt5.account_info()
            balance = account.balance
            equity = account.equity
            account_number = account.login
            server_name=account.server
            currency = account.currency
            watch_time = mt5.symbol_info_tick("EURUSD").time
            watch_time = datetime.fromtimestamp(watch_time)

            # Save data to MongoDB
            accounts_col.insert_one({
                "account_number": account_number,
                "balance": balance,
                "equity": equity,
                "server_name":server_name,
                "currency": currency,
                "market_watch_time": watch_time
            })

            print("Accounts data saved successfully!")
        mt5.shutdown()
        time.sleep(60)

def start_data_fetching_thread():
    loop = asyncio.new_event_loop()
    t = threading.Thread(target=start_loop, args=(loop,))
    t.start()
