import yfinance as yf
from indicators import calculate_indicators


def scan_symbol(symbol):

    df = yf.download(
        symbol,
        period="2y",
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

    signal = (
        close.iloc[-1] > sma50.iloc[-1]
        and close.iloc[-1] > sma200.iloc[-1]
        and 40 <= rsi.iloc[-1] <= 70
        and volume_growth > 1.10
    )

    return {
        "symbol": symbol,
        "close": round(float(close.iloc[-1]), 2),
        "rsi": round(float(rsi.iloc[-1]), 1),
        "above_sma50": close.iloc[-1] > sma50.iloc[-1],
        "above_sma200": close.iloc[-1] > sma200.iloc[-1],
        "volume_growth": round(float(volume_growth), 2),
        "rel_volume": round(float(rel_volume), 2),
        "distance_to_high": round(float(distance_to_high), 1),
        "signal": signal
    }
