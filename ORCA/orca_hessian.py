import pandas as pd
import numpy as np
from numpy import linalg as LA

df = pd.read_csv("C:/Users/henri/Documents/Projects/Python-Lessons/ORCA/orca.hess", delim_whitespace=True).dropna() 
chunks = len(df) / (df.index.max() + 1)  

v = np.hstack(np.vsplit(df.values, chunks))

df = pd.DataFrame(v)
df_eig = LA.eig(np.array(df))

print("=" * 80)
print(df_eig)
print("=" * 80)