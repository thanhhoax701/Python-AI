from fractions import Fraction

import math
import pandas as pd

def H(X: pd.Series, C: float = 1, base: float = 2) -> float:
    return X.apply(lambda p: -p*math.log(p, base)).sum()

def main() -> None:
    df = pd.read_csv("./entrophy_data.csv")
    print(df, '\n')

    df = df.applymap(lambda x: float(Fraction(x)))
    print(df)

    for var in df.columns:
        ans = H(df[var])
        print("\nH({})\n\t={}\n\t={}".format(var, Fraction(ans), ans))

if __name__ == "__main__":
    main()