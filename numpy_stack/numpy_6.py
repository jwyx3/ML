# coding: utf-8
X = []
import numpy as np
for line in open("data_2d.csv"):
    row = line.split(',')
    sample = map(float, row)
    X.append(sample)
    
X
X = np.array(X)
X.shape
