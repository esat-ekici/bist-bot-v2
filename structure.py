import pandas as pd

LEFT = 3
RIGHT = 3


def detect_swings(df):

    df = df.copy()

    df["SwingHigh"] = False
    df["SwingLow"] = False

    highs = df["High"].values
    lows = df["Low"].values

    for i in range(LEFT, len(df)-RIGHT):

        h = highs[i]

        if h == max(highs[i-LEFT:i+RIGHT+1]):
            df.iat[i, df.columns.get_loc("SwingHigh")] = True

        l = lows[i]

        if l == min(lows[i-LEFT:i+RIGHT+1]):
            df.iat[i, df.columns.get_loc("SwingLow")] = True

    return df
