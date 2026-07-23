from downloader import download
from indicators import calculate
from scoring import score

with open("stocks.txt") as f:
    stocks = [x.strip() for x in f.readlines()]

results = []

for symbol in stocks:

    print(symbol)

    df = download(symbol)

    if df is None:
        continue

    df = calculate(df)

    s = score(df)

    s["Symbol"] = symbol

    results.append(s)

results = sorted(
    results,
    key=lambda x: x["TOTAL"],
    reverse=True
)

print()

print("=" * 50)

for r in results:

    print(
        f'{r["Symbol"]:10} '
        f'{r["TOTAL"]:3} '
        f'Trend:{r["Trend"]:2} '
        f'RSI:{r["RSI"]:2} '
        f'RVOL:{r["RVOL"]:2} '
        f'Mom:{r["Momentum"]:2}'
    )
