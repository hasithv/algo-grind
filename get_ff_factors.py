import pandas as pd
from datetime import datetime
import csv


def get_ff_factors():
    df = pd.read_csv("month_factors.csv")

    df.Date = pd.to_datetime(df.Date, format="%d-%m-%Y")
    df = df.resample('M', on='Date').mean()
    df.to_csv("month_factors.csv", line_terminator="", encoding='utf-8')


def add_dashes(d):
    return '%s-%s-%s' % (d[8:], d[5:7], d[:4])


if __name__ == '__main__':
    get_ff_factors()
