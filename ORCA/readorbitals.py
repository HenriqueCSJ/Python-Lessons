import numpy as np
import scipy as sp

with open('C:/Users/henri/Documents/Projects/Python-Lessons/ORCA/methane.out', 'r') as orca_out:
    outputs = orca_out.read()
    for lines in outputs:
        print(lines, end='')