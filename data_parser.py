import time
import requests

# replace the values
apikey="9NX4ZJK5X6GWNTZL"
stock = "RELIANCE"
index = "BSE"



url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}.{}&outputsize=full&apikey={}'.format(stock,index,apikey)
r = requests.get(url)
data = r.json()



# print(data["Time Series (Daily)"])

date_by_data = data["Time Series (Daily)"]


dates = list(date_by_data.keys())

for i in dates[:5]:
    index = dates.index(i)
    date = i
    date_data = date_by_data[i]
    # print(date_data)

    volume = date_data["6. volume"]
    print("Stock volume for date {} is {}".format(date, volume))

    if index > 0:
        previous_date_data = date_by_data[dates[index-1]]
        print(date_data["6. volume"])
        print(previous_date_data["6. volume"])

        diff = int(date_data["6. volume"]) - int(previous_date_data["6. volume"])

        print("Volume difference", diff)





