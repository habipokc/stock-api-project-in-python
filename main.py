import requests



STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


api_key = "YOUR API KEY"

stock_params = {
     "function": "TIME_SERIES_INTRADAY",
     "symbol": STOCK_NAME,
     "interval": "5min",
     "apikey": api_key
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()
data_list = [value for (key,value) in stock_data.items()]
print(data_list)






