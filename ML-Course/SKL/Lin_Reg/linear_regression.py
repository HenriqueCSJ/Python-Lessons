# Estudar regressão linear
# Maísa procuradoria problema de rede

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

df = pd.read_csv("/home/henrique/Coding/Python/ML-Course/SKL/USA_Housing.csv")

df.head()
print(df.info())

df.describe()
print(df.columns)

sns.pairplot(df)
sns.distplot(df["Price"])
sns.heatmap(df.corr(), annot=True)

X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
        'Avg. Area Number of Bedrooms', 'Area Population' , 'Price']]

X.head()

X_train, X_test, y_train, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=101)
