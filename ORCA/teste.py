# import pandas as pd
# import numpy as np
# from numpy import linalg as LA

# matrix_A = np.array([[1, 2], [3, 4]])
# print(matrix_A)
# eigen_matrix = LA.eigh(np.array(matrix_A))
# print(eigen_matrix)
# x, y = eigen_matrix
# print(x)
# print(y)

import pandas as pd
import numpy as np
from numpy import linalg

df = pd.read_csv("C:/Users/henri/Documents/Projects/Python-Lessons/ORCA/orca.hess", delim_whitespace=True).dropna() 
chunks = len(df) / (df.index.max() + 1)  

v = np.hstack(np.vsplit(df.values, chunks))

df = pd.DataFrame(v)
df_eig_x, df_eig_y = linalg.eig(np.array(df))
print(df_eig_x)
print("-" * 80)
print(df_eig_y)