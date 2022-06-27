import pandas as pd
from os import listdir
from os.path import isfile, join


def get_constituents():
    mypath = "csv/"
    df = pd.DataFrame()
    df["ticker"] = [f[0:-4] for f in listdir(mypath) if isfile(join(mypath, f))]
    return df


if __name__ == "__main__":
    get_constituents().to_csv("constituents.csv", encoding="utf-8", line_terminator="", index=False)
