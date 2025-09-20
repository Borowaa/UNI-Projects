import requests

import json

import pandas as pd

import mplfinance as mpl

import matplotlib.pyplot as plt

url = 'https://www.mexc.com/open/api/v2/market/kline?symbol=ETH_USDT&interval=1m&limit=500'

response = requests.get(url)

responseBodyJson = json.loads(response.text)

candlesData = responseBodyJson.get("data", [])

if not candlesData:

    print("Brak danych w odpowiedzi API.")

    exit()

formattedcandlesData = []

for candle in candlesData:

    formattedcandlesData.append({

        'time': candle[0],

        'open': float(candle[1]),

        'high': float(candle[2]),

        'low': float(candle[3]),

        'close': float(candle[4])

    })

df = pd.json_normalize(formattedcandlesData)

df.time = pd.to_datetime(df.time, unit='s')

df = df.set_index("time")

df.rename(columns={"open": "Open", "high": "High", "low": "Low", "close": "Close"}, inplace=True)

print(df.tail())

print(df.describe())

def standardize(series):

    return (series - series.mean()) / series.std()

df['Open_std'] = standardize(df['Open'])

df['Close_std'] = standardize(df['Close'])

if len(df) < 20:

    print("Za mało danych, aby znaleźć dopasowanie.")

    exit()

pattern = df.iloc[-10:]

for i in range(len(df) - 20):

    segment = df.iloc[i:i + 10]

    diff_open = abs(pattern['Open_std'].values - segment['Open_std'].values)

    diff_close = abs(pattern['Close_std'].values - segment['Close_std'].values)

    if (diff_open < 0.2).all() and (diff_close < 0.2).all():

        print("Dopasowanie znalezione na indeksie:", i)

        mpl.plot(segment, type="candle", title="Segment", style="binance")

        mpl.plot(pattern, type="candle", title="Pattern", style="binance")

        plt.show()

        break

else:

    print("Nie znaleziono dopasowania.")