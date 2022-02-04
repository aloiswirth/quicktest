# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_core.ipynb (unless otherwise specified).

__all__ = ['data1', 'data2', 'df1', 'df2', 'curr_dir', 'real_path']

# Cell
import pandas as pd
import os
import nbdev

# Cell

data1 ={
    "ID" : [ 1, 2, 3, 4, 5],
    "age" : [ 0, 0, 0, 0, 0]
}

data2 = {
    "ID" : [ 1, 2, 3, 4, 5],
    "age" : [ 6, 7, 8, 9, 10]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Cell
curr_dir = os.getcwd()
print(curr_dir)

# Cell
real_path = os.path.realpath('.')
print(real_path)

import os
dir_file = os.path.dirname(__file__)
print(dir_file)

d = os.path.dirname(dir_file)
print(d)