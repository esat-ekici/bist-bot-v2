from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator
from ta.volatility import AverageTrueRange

def calculate(df):

    df["EMA20"] = EMAIndicator(df.Close,20).ema_indicator()
    df["EMA50"] = EMAIndicator(df.Close,50).ema_indicator()
    df["EMA200"] = EMAIndicator(df.Close,200).ema_indicator()

    df["RSI"] = RSIIndicator(df.Close,14).rsi()

    atr = AverageTrueRange(
        df.High,
        df.Low,
        df.Close,
        14
    )

    df["ATR"] = atr.average_true_range()

    df["RVOL"] = df.Volume / df.Volume.rolling(20).mean()

    return df
