import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split

train = pd.read_csv("titanic_train.csv")
print(train.head())

print(train.info())
print(train.isnull())

sns.heatmap()