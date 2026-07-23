import numpy as np


def score(df):

    last = df.iloc[-1]

    score = 0
    details = {}

    # -------------------------
    # EMA Trend (20)
    # -------------------------

    ema_score = 0

    if last["EMA20"] > last["EMA50"]:
        ema_score += 8

    if last["EMA50"] > last["EMA200"]:
        ema_score += 8

    if last["Close"] > last["EMA20"]:
        ema_score += 4

    score += ema_score
    details["Trend"] = ema_score

    # -------------------------
    # RSI (10)
    # -------------------------

    rsi = last["RSI"]

    rsi_score = 0

    if 55 <= rsi <= 70:
        rsi_score = 10

    elif 50 <= rsi < 55:
        rsi_score = 7

    elif 45 <= rsi < 50:
        rsi_score = 4

    score += rsi_score
    details["RSI"] = rsi_score

    # -------------------------
    # Relative Volume (15)
    # -------------------------

    rvol = last["RVOL"]

    if rvol >= 2:
        rvol_score = 15

    elif rvol >= 1.5:
        rvol_score = 12

    elif rvol >= 1.2:
        rvol_score = 8

    elif rvol >= 1:
        rvol_score = 5

    else:
        rvol_score = 0

    score += rvol_score
    details["RVOL"] = rvol_score

    # -------------------------
    # Momentum (15)
    # -------------------------

    momentum = 0

    change5 = (
        last["Close"] /
        df["Close"].iloc[-6]
        - 1
    ) * 100

    if change5 > 10:
        momentum = 15

    elif change5 > 6:
        momentum = 12

    elif change5 > 3:
        momentum = 8

    elif change5 > 0:
        momentum = 4

    score += momentum
    details["Momentum"] = momentum

    # -------------------------
    # ATR (10)
    # -------------------------

    atr_percent = last["ATR"] / last["Close"] * 100

    atr_score = 10

    if atr_percent > 8:
        atr_score = 4

    elif atr_percent > 6:
        atr_score = 7

    score += atr_score
    details["ATR"] = atr_score

    details["TOTAL"] = score

    return details
