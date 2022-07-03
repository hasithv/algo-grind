import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import statsmodels.api as sm


def get_lin_regress():
    smb = pd.read_csv("test regressions.csv")["Mkt-RF"]
    del_smb = pd.read_csv("test regressions.csv")["del smb"]

    X = smb.values
    Y = del_smb.values

    X = sm.add_constant(X)

    model = sm.OLS(Y,X).fit()

    print(model.summary())

if __name__ == '__main__':
    get_lin_regress()
