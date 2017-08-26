# coding: utf-8
get_ipython().magic(u'load pandas_1.py')
# %load pandas_1.py
import pandas as pd
X = pd.read_csv("data_2d.csv", header=None)
type(X)
X.info
X.info()
X.head()
X.head(10)
M = X.as_matrix()
type(M)
X[0].shape
X.head()
# Numpy: X[0] -> 0th row
# Pandas: X[0] -> colume has that name 0
type(X[0])
# how to get row
X.iloc[0]
X.ix[0]
type(X.iloc[0])
X[[0,2]]
X[ X[0] < 5 ]
X[0] < 5
type(X[0] < 5)
