# coding: utf-8
get_ipython().magic(u'load pandas_3.py')
# %load pandas_3.py
import pandas as pd
df = pd.read_csv("international-airline-passengers.csv", header=None)
df = pd.read_csv("international-airline-passengers.csv", engine="python", skipfooter=3)
# skipfootor doesn't work with default engine, so use python
df.columns
df.columns = ["month", "passengers"]
df.columns
df.passengers
df["passengers"]
# add one column
df['ones'] = 1
df.head()
from datetime import datetime
datetime.strptime("1949-05", "%Y-%m")
df['dt'] = df.apply(lambda row: datetime.strptime(row['month'], "%Y-%m"), axis=1)
df.info()
