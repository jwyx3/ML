# coding: utf-8
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
