import yfinance as yf
from telegram_sender import send_message

ticker = yf.Ticker("ASELS.IS")

price = ticker.history(period="5d")["Close"].iloc[-1]

message = (
    f"📊 Veri Testi\n\n"
    f"Hisse: ASELS\n"
    f"Son Fiyat: {price:.2f}"
)

send_message(message)
