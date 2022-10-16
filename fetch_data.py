import requests
import datetime
from config import api_key


endpt = ("https://api.tdameritrade.com/v1/marketdata/GME/pricehistory")

payload = {
    'apikey': api_key,
    'periodType': 'month',
    'frequencyType': 'daily',
    'frequency': '1',
    # 'period': '10',
    'endDate': '1662021000000',
    'startDate': '1598949000000',
    'needExtendedHoursData': 'false'
}

content = requests.get(url = endpt, params = payload)
data = content.json()

# def close_data(d):
#     for i in data:
#         print(d[1]['close'])


# print(data['candles'][0]['close'] * 4)


for x in data['candles']:
    print(x['close'] * 4)
    print(datetime.date.fromtimestamp(x['datetime']))


# convert to date
# dt = datetime.date.fromtimestamp(1662062280)
# print(dt)