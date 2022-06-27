import pandas as pd
from datetime import datetime
import csv


def get_ff_factors():
    df = pd.read_csv("3_factors.csv")
    df["Date"] = df["Date"].apply(lambda x: add_dashes(x))
    df.to_csv("3_factors.csv", index=False, line_terminator="", encoding='utf-8')

def add_dashes(d):
    return '%s-%s-%s' % (d[8:], d[5:7], d[:4])


if __name__ == '__main__':
    get_ff_factors()
