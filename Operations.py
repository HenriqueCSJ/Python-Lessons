import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()

print(df)

print(df.head())
print(df["col2"].unique())

print(len(df["col2"].unique()))

print(df["col2"].nunique())

print(df["col2"].value_counts())

def times2(x):
    return x*2

df["col2"].apply(times2)

df["col3"].apply(len)
df["col3"].apply(lambda x: x*2)
df["col2"].apply(lambda x: x*2)
df.drop("col1", axis=1)
df
df.columns
df.index

df.sort_values(by="col2")

df.isnull()

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print(data)
df

df.pivot_table(values="D", index=["A", "B"], columns=["C"])