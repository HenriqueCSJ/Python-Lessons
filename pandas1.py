#%%
import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4), ["A", "B", "C", "D", "E"], ["W", "X", "Y", "Z"])
print(df)

df["new"] = df["W"] + df["X"]

print(df)
print(df.drop("new", axis=1))
df.drop("new", axis=1, inplace=True)
print(df)

df.drop("E", axis=0)

df.loc["A"]
df.iloc[2]
df.loc["B", "Y"]

df.loc[["A", "C"], ["W", "Z"]]