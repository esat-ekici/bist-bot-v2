import yfinance as yf
from indicators import calculate_indicators


def ema(series, period):
    return series.ewm(span=period, adjust=False).mean()


def scan_symbol(symbol):

    df = yf.download(
        symbol,
        period="3y",
        auto_adjust=True,
        progress=False
    )

    close = df[("Close", symbol)]
    volume = df[("Volume", symbol)]

    sma50, sma200, rsi = calculate_indicators(close)

    avg20 = volume.tail(20).mean()
    avg60 = volume.tail(60).mean()

    volume_growth = avg20 / avg60
    rel_volume = volume.iloc[-1] / avg20

    high52 = close.tail(252).max()

    distance_to_high = (
        (high52 - close.iloc[-1])
        / high52
    ) * 100

    # ------------------
    # HAFTALIK MACD
    # ------------------

    weekly_close = close.resample("W-FRI").last()

    ema12 = ema(weekly_close, 12)
    ema26 = ema(weekly_close, 26)

    macd = ema12 - ema26
    signal = ema(macd, 9)

    macd_positive = macd.iloc[-1] > signal.iloc[-1]

    # ------------------
    # PUANLAMA
    # ------------------

    score = 0

    if close.iloc[-1] > sma200.iloc[-1]:
        score += 3

    if close.iloc[-1] > sma50.iloc[-1]:
        score += 2

    if 45 <= rsi.iloc[-1] <= 70:
        score += 1

    if volume_growth > 1:
        score += 2

    if distance_to_high < 15:
        score += 2

    if macd_positive:
        score += 3

    return {
        "symbol": symbol,
        "close": round(float(close.iloc[-1]), 2),
        "score": score,
        "rsi": round(float(rsi.iloc[-1]), 1),
        "distance_to_high": round(float(distance_to_high), 1),
        "volume_growth": round(float(volume_growth), 2),
        "macd_positive": macd_positive
    }
