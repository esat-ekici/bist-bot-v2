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

    sma50, sma200, rsi = calculate_indicators(close)

    return {
        "symbol": symbol,
        "close": float(close.iloc[-1]),
        "rsi": float(rsi.iloc[-1]),
        "above_sma50": close.iloc[-1] > sma50.iloc[-1],
        "above_sma200": close.iloc[-1] > sma200.iloc[-1]
    }
