from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.views.generic import  TemplateView,ListView
from django.conf import settings
import MetaTrader5 as mt5
from .models import Account
from datetime import datetime
import datetime
from django.core.serializers.json import DjangoJSONEncoder
from bson import Decimal128
import simplejson as json
from decimal import Decimal
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
import pymongo
from datetime import datetime, timedelta
import pymt5
# Create your views here.

class HomePageView(ListView):
    model=Account
    context_object_name="accounts"
    template_name="mainapp/index.html"




@csrf_exempt
def fetchdata(request):
    client = pymongo.MongoClient(settings.MONGO_DB)
    db = client["las4zan"]
    account_collection = db["accounts"]
    # print(account_collection)
    accounts = []
    for account in account_collection.find():
        accounts.append({
            'account_number': account['account_number'],
            'equity': float(account['equity']),
            'balance': float(account['balance']),
            'server_name': account['server_name'],
            'market_watch_time': account['market_watch_time'].strftime('%Y-%m-%d %H:%M:%S')
        })
    return JsonResponse({"accounts":accounts}, safe=False)

def dashboard(request):

    return render(request, 'mainapp/dashboard.html')


@csrf_exempt
def dashboard_fetchdata(request):
    client = pymongo.MongoClient(settings.MONGO_DB)
    db = client["las4zan"]
    account_collection = db["accounts"]
    
    account1 = []
    account2 = []
    account3 = []
    accounts = []
    for account in account_collection.find({"server_name": "ICMarketsEU-Demo"}):
        accounts.append({
            'account_number': account['account_number'],
            'equity': float(account['equity']),
            'balance': float(account['balance']),
            'server_name': account['server_name'],
            'market_watch_time': account['market_watch_time'].strftime('%Y-%m-%d %H:%M:%S')
        })
    for account in account_collection.find({"account_number":22014542,"server_name":"Deriv-Demo"}):
        account1.append({
            'account_number': account['account_number'],
            'equity': float(account['equity']),
            'balance': float(account['balance']),
            'server_name': account['server_name'],
            'market_watch_time': account['market_watch_time'].strftime('%Y-%m-%d %H:%M:%S')
        })
    for account in account_collection.find({"account_number":51135132,"server_name":"ICMarketsEU-Demo"}):
        account2.append({
            'account_number': account['account_number'],
            'equity': float(account['equity']),
            'balance': float(account['balance']),
            'server_name': account['server_name'],
            'market_watch_time': account['market_watch_time'].strftime('%Y-%m-%d %H:%M:%S')
        })
    for account in account_collection.find({"account_number":51135134,"server_name": "ICMarketsEU-Demo"}):
        account3.append({
            'account_number': account['account_number'],
            'equity': float(account['equity']),
            'balance': float(account['balance']),
            'server_name': account['server_name'],
            'market_watch_time': account['market_watch_time'].strftime('%Y-%m-%d %H:%M:%S')
        })

    return JsonResponse({"accounts":accounts,"account1":account1,"account2":account2,"account3":account3}, safe=False)

