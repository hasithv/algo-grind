import pandas as pd

import fama
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    full_df = pd.DataFrame(columns=["ticker", "max-month", "max-r^2"])
    full_df["ticker"] = pd.read_csv("constituents.csv")["ticker"]
    full_df = full_df.set_index("ticker")

    for ticker in full_df.index:
        try:
            months_df = pd.DataFrame(columns=["month range", "r^2"])
            for m in range(2, 19):
                months_df.loc[m-2] = [m, fama.run_fama(ticker, m)[1]]

            full_df.loc[ticker] = months_df.loc[months_df['r^2'].idxmax()]
        except:
            print(ticker)

    # x = fama.run_fama("MSFT", 12)[0]

    """
    plt.subplot(211)
    plt.bar(x.index, x["ER"], label="ER", alpha=0.5)
    plt.bar(x.index, x["roi"], label="roi", alpha=0.5)
    plt.legend(loc="upper right")

    plt.subplot(212)
    plt.scatter(x["roi"], x["ER"])
    plt.show()
    """
