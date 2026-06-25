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

        message += (
            f"{symbol}\n"
            f"Satırlar: {len(df)}\n"
            f"Sütunlar: {list(df.columns)}\n\n"
        )

    except Exception as e:

        message += f"{symbol} : {str(e)}\n\n"

send_message(message[:4000])
