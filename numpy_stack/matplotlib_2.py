# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
A = pd.read_csv('data_1d.csv', header=None).as_matrix()
x = A[:,0]
y = A[:,1]
x
y
plt.scatter(x, y)
plt.show()
x_line = np.linspace(0, 100, 100)
y_line = 2 * x_line + 1
plt.scatter(x, y)
plt.scatter(x_line, y_line)
plt.show()
