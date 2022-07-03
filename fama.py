import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import statsmodels.api as sm


def next_smb(smb):
    return (1 - 0.9702) * smb - 0.0033


def next_hml(hml):
    return (1 - 0.7048) * hml + 0.0088


def next_mktrf(mktrf):
    return (1 - 0.9291) * mktrf + 0.021


def next_factors(factors):
    return [[next_mktrf(factors[0]), next_smb(factors[1]), next_hml(factors[2])]]


def run_fama(ticker, months):
    ticker_df = pd.read_csv("monthly-data/" + ticker + "-m.csv", index_col="Date")
    ticker_df = ticker_df.drop(ticker_df.columns[0], axis=1)
    factors_df = pd.read_csv("month_factors.csv", index_col="Date")

    first_date = max(ticker_df.index[1], factors_df.index[1])
    last_date = min(ticker_df.index[-1], factors_df.index[-1])

    ticker_df = ticker_df[first_date:last_date]
    factors_df = factors_df[first_date:last_date]
    ticker_df["ER"] = np.nan

    if ticker_df.shape[0] >= 24:
        for i in range(months, ticker_df.shape[0]):
            X = factors_df[i - months:i][["Mkt-RF", "SMB", "HML"]].values
            y = ticker_df[i - months:i]["roi"] - factors_df[i - months:i]["RF"].values

            model = linear_model.LinearRegression()
            model.fit(X, y)

            ticker_df["ER"][i] = model.predict(next_factors(factors_df.iloc[i - 1][0:3]))

        rx = ticker_df[months:-1][["roi"]]
        ry = ticker_df[months:-1][["ER"]]
        rmodel = linear_model.LinearRegression()
        rmodel.fit(rx, ry)

        return ticker_df, rmodel.score(rx, ry)
    else:
        return ticker_df, -99.99

if __name__ == "__main__":
    """
    tickers = pd.read_csv("constituents.csv")
    analysis_df = pd.DataFrame(columns=["ticker", "r^2", "adj r^2"])
    analysis_df = analysis_df.set_index("ticker")

    for ticker in tickers["ticker"]:
        ticker_df = pd.read_csv("monthly-data/" + ticker + "-m.csv", index_col="Date")
        ticker_df = ticker_df.drop(ticker_df.columns[0], axis=1)
        factors_df = pd.read_csv("month_factors.csv", index_col="Date")

        first_date = max(ticker_df.index[0], factors_df.index[0])
        last_date = min(ticker_df.index[-1], factors_df.index[-1])

        ticker_df = ticker_df[first_date:last_date]
        ticker_df = ticker_df[first_date:last_date]

        if ticker_df.shape[0] >= 24:
            X = factors_df[["Mkt-RF", "SMB", "HML"]]
            y = ticker_df["roi"] - factors_df["RF"]

            X = sm.add_constant(X)
            ff_model = sm.OLS(y, X, missing="drop").fit()
            # intercept, b1, b2, b3 = ff_model.params

            analysis_df.loc[ticker] = [ff_model.rsquared, ff_model.rsquared_adj]
"""
    x, r2 = run_fama("MSFT", 12)

    plt.subplot(211)
    plt.bar(x.index, x["ER"], label="ER", alpha=0.5)
    plt.bar(x.index, x["roi"], label="roi", alpha=0.5)
    plt.legend(loc="upper right")

    plt.subplot(212)
    plt.scatter(x["roi"], x["ER"])
    plt.show()
