import requests
import jeson
import pandas as pd
import mplfinance as mpl


def fetch_candles(url: str) -> list:

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data.get("data", [])


def format_candles(raw_candles: list) -> list:

    formatted = []
    for candle in raw_candles:
        ts, o, c, h, l = candle[0], candle[1], candle[2], candle[3], candle[4]
        formatted.append({
            'time': ts,
            'open': float(o),
            'close': float(c),
            'high': float(h),
            'low': float(l)
        })
    return formatted


def prepare_dataframe(formatted_candles: list) -> pd.DataFrame:

    df = pd.json_normalize(formatted_candles)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.set_index('time', inplace=True)
    return df


def plot_candles(df: pd.DataFrame, title: str = 'Candle chart') -> None:

    mpl.plot(
        df,
        type='candle',
        title=title,
        style='yahoo',
        mav=(3, 6, 9)
    )


if __name__ == '__main__':
    # URL endpoint zwracający dane świec z API MEXC
    url = (
        'https://www.mexc.com/open/api/v2/market/kline'
        '?symbol=TRUMP1_USDT&interval=60m&limit=10'
    )

    # Pobieranie surowych danych świec
    candles_data = fetch_candles(url)

    # Formatowanie danych do postaci wymaganej przez pandas/mplfinance
    formatted = format_candles(candles_data)
    df = prepare_dataframe(formatted)

    # Weryfikacja poprawności ramki danych
    print("Columns:", df.columns.tolist())
    print(df.head())

    # Rysowanie wykresu świecowego
    plot_candles(df, title='TRUMP1/USDT 60m Candle Chart')