from symbols import SYMBOLS
from scanner import scan_symbol
from telegram_sender import send_message

message = "📊 BIST RAPORU\n\n"

for symbol in SYMBOLS:

    try:

        result = scan_symbol(symbol)

        message += (
            f"{result['symbol']}\n"
            f"Fiyat: {result['close']:.2f}\n"
            f"RSI: {result['rsi']:.1f}\n"
            f"SMA50: {'✅' if result['above_sma50'] else '❌'}\n"
            f"SMA200: {'✅' if result['above_sma200'] else '❌'}\n\n"
        )

    except Exception as e:

        message += f"{symbol}: HATA\n\n"

send_message(message[:4000])
