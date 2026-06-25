from symbols import SYMBOLS
from scanner import scan_symbol
from telegram_sender import send_message

results = []

for symbol in SYMBOLS:

    try:

        result = scan_symbol(symbol)

        results.append(result)

    except Exception:

        pass

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

message = "📊 BIST KURUMSAL TOPLAMA TARAMASI\n\n"

for r in results:

    message += (
        f"{r['symbol']}\n"
        f"Skor: {r['score']}/13\n"
        f"RSI: {r['rsi']}\n"
        f"Hacim20/60: {r['volume_growth']}\n"
        f"52H Zirve Uzaklık: %{r['distance_to_high']}\n"
        f"Haftalık MACD: {'✅' if r['macd_positive'] else '❌'}\n\n"
    )

send_message(message[:4000])
