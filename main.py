import yfinance as yf
from telegram_sender import send_message
from symbols import SYMBOLS

message = "📊 BIST TARAMA TESTİ\n\n"

for symbol in SYMBOLS:

    try:

        df = yf.download(
            symbol,
            period="3mo",
            auto_adjust=True,
            progress=False
        )

        close = float(df["Close"].iloc[-1])

        message += f"{symbol} : {close:.2f}\n"

    except Exception as e:

        message += f"{symbol} : HATA\n"

send_message(message)
