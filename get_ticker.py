import pandas as pd
from os import listdir
from os.path import isfile, join


def get_constituents():
    mypath = "csv/"
    df = pd.DataFrame()
    df["ticker"] = [f[0:-4] for f in listdir(mypath) if isfile(join(mypath, f))]
    return df


def make_monthly():
    tickers = pd.read_csv("constituents.csv")
    for ticker in tickers["ticker"]:
        df = pd.read_csv("csv/" + ticker + ".csv")
        df.Date = pd.to_datetime(df.Date, format="%d-%m-%Y")
        df = df.resample('M', on='Date').mean()
        df.to_csv("monthly-data/" + ticker + "-m.csv")


def create_roi(directory=""):
    tickers = pd.read_csv("constituents.csv")
    for ticker in tickers["ticker"]:
        df = pd.read_csv(directory + ticker + "-m.csv")
        df["roi"] = (df["Adjusted Close"]-df["Adjusted Close"][0])/df["Adjusted Close"][0]
        df.to_csv(directory + ticker + "-m.csv")


if __name__ == "__main__":
    # get_constituents().to_csv("constituents.csv", encoding="utf-8", line_terminator="", index=False)
    create_roi(directory="monthly-data/")
