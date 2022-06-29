import fama
import numpy as np


if __name__ == "__main__":
    x = fama.run_fama("AAPL", 12)
    print(x[1])
