# coding: utf-8
get_ipython().magic(u'load matplotlib_2.py')
# %load matplotlib_2.py
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
plt.hist(x)
plt.show()
R = np.random.random(1000)
plt.hist(R)
plt.show()
plt.hist(R, bins=20)
plt.show()
y_actual = 2*x + 1
residuals = y - y_actual
plt.hist(residuals)
plt.show()
