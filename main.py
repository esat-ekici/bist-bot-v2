from symbols import SYMBOLS
from scanner import scan_symbol
from telegram_sender import send_message

message = "📊 BIST RAPORU\n\n"

for symbol in SYMBOLS:

    try:

        result = scan_symbol(symbol)

        message += (
            f"{result['symbol']}\n"
            f"Fiyat: {result['close']}\n"
            f"RSI: {result['rsi']}\n"
            f"SMA50: {'✅' if result['above_sma50'] else '❌'}\n"
            f"SMA200: {'✅' if result['above_sma200'] else '❌'}\n"
            f"Hacim20/60: {result['volume_growth']}\n"
            f"RelVol: {result['rel_volume']}\n"
            f"52H Zirve Uzaklık: %{result['distance_to_high']}\n"
            f"Sinyal: {'🔥' if result['signal'] else '-'}\n\n"
        )

    except Exception as e:

        message += f"{symbol}: HATA ({str(e)})\n\n"

send_message(message[:4000])
