import yfinance as yf
from telegram_sender import send_message

symbol = "ASELS.IS"

df = yf.download(
    symbol,
    period="5d",
    auto_adjust=True,
    progress=False
)

last_close = float(df["Close"].iloc[-1])

message = (
    f"📊 Veri Testi\n\n"
    f"Hisse: {symbol}\n"
    f"Son Fiyat: {last_close:.2f}"
)

send_message(message)
