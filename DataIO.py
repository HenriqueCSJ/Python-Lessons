import pandas as pd

pd.read_csv("~/Coding/Python/example")

pd.read_excel("/home/henrique/Coding/Python/Excel_Sample.xlsx")

df = pd.read_csv("~/Coding/Python/example")
df.to_csv("My_output", index=False)

pd.read_csv("~/Coding/Python/My_ouput")