import requests
import json
import pandas as pd
import mplfinance as mpl
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = Tk()
root.title('Crypto Candle Chart')
canvas = Canvas(root, height=800, width=600)
canvas.pack()


background_image = PhotoImage(file='altum.png')
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


frame = Frame(root, bg='#ffffff')
frame.place(relx=0.5, rely=0.3, relwidth=0.8, relheight=0.3, anchor='n')


labelSymbol = Label(frame, text="Symbol")
labelSymbol.place(relx=0.05, rely=0.05, relwidth=0.18, relheight=0.2)

entrySymbol = Entry(frame, font=40)
entrySymbol.place(relx=0.25, rely=0.05, relwidth=0.3, relheight=0.2)
entrySymbol.insert(0, "ETH_USDT") # Domyślna wartość

labelInterval = Label(frame, text="Interval")
labelInterval.place(relx=0.05, rely=0.4, relwidth=0.18, relheight=0.2)

entryInterval = Entry(frame, font=40)
entryInterval.place(relx=0.25, rely=0.4, relwidth=0.3, relheight=0.2)
entryInterval.insert(0, "1m") # Domyślna wartość

labelLimit = Label(frame, text="Limit")
labelLimit.place(relx=0.05, rely=0.75, relwidth=0.18, relheight=0.2)

entryLimit = Entry(frame, font=40)
entryLimit.place(relx=0.25, rely=0.75, relwidth=0.3, relheight=0.2)
entryLimit.insert(0, "500") # Domyślna wartość


labelThreshold = Label(frame, text="Threshold")
labelThreshold.place(relx=0.6, rely=0.05, relwidth=0.18, relheight=0.2)

entryThreshold = Entry(frame, font=40)
entryThreshold.place(relx=0.8, rely=0.05, relwidth=0.15, relheight=0.2)
entryThreshold.insert(0, "0.2") # Domyślna wartość


def generate_chart():
symbol = entrySymbol.get()
interval = entryInterval.get()
limit = entryLimit.get()
threshold = float(entryThreshold.get())

url = f'https://www.mexc.com/open/api/v2/market/kline?symbol={symbol}&interval={interval}&limit={limit}'
response = requests.get(url)
responseBodyJson = json.loads(response.text)

candlesData = responseBodyJson.get("data", [])
if not candlesData:
print("Brak danych! Sprawdź poprawność parametrów.")
return

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

plot_in_gui(df)

find_pattern(df, threshold)



def plot_in_gui(df):
fig, ax = plt.subplots(figsize=(8, 5))

mpl.plot(df, type="candle", style="yahoo", title="Wykres świecowy")


canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=BOTH, expand=True)


root.update_idletasks()



def find_pattern(df, threshold):
pattern = df.iloc[-10:]

for i in range(len(df) - 20):
segment = df.iloc[i:i + 10]
diff_open = abs(pattern["Open"].values - segment["Open"].values)
diff_close = abs(pattern["Close"].values - segment["Close"].values)

if (diff_open < threshold).all() and (diff_close < threshold).all():
print(f"Dopasowanie znalezione na indeksie: {i}")
plot_in_gui(segment)
break
else:
print("Nie znaleziono dopasowania.")



generateButton = Button(frame, text="Generuj wykres", command=generate_chart)
generateButton.place(relx=0.6, rely=0.75, relwidth=0.35, relheight=0.2)

root.mainloop()