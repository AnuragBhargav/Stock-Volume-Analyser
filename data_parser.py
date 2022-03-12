

import time
import requests
from statistics import mean

# replace the values
apikey=""
stock = "RELIANCE"
index = "BSE"



url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}.{}&outputsize=full&apikey={}'.format(stock,index,apikey)
r = requests.get(url)
data = r.json()


date_by_data = data["Time Series (Daily)"]


dates = list(date_by_data.keys())

volume_list = []

for date in dates[:20]:

    date_data = date_by_data[date]

    volume = date_data["6. volume"]

    volume_list.append(int(volume))

today_data = date_by_data[dates[0]]["6. volume"]

twenty_avg= mean(volume_list)

if int(today_data) > int(twenty_avg):
    print("Today the volume is greater than 20 days avg")




