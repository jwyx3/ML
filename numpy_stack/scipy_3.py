# coding: utf-8
get_ipython().magic(u'load scipy_2.py')
# %load scipy_2.py
get_ipython().magic(u'load scipy_1.py')
# %load scipy_1.py
from scipy.stats import norm
norm.pdf(0)
norm.pdf(0, loc=5, scale=10)
import numpy as np
r = np.random.randn(10)
norm.pdf(r)
# Joint probability vs. log of joint probability of data samples (+ fastrer than *)
# Log of Gaussian PDF (much faster since no exponential!)
norm.logpdf(r)
norm.cdf(r)
norm.logcdf(r)
import matplotlib.pyplot as plt
r = np.random.randn(10000)
plt.hist(r, bins=100)
plt.show()
r = 10 * np.random.randn(10000) + 5
plt.hist(r, bins=100)
plt.show()
# %load scipy_1.py
from scipy.stats import norm
norm.pdf(0)
norm.pdf(0, loc=5, scale=10)
import numpy as np
r = np.random.randn(10)
norm.pdf(r)
# Joint probability vs. log of joint probability of data samples (+ fastrer than *)
# Log of Gaussian PDF (much faster since no exponential!)
norm.logpdf(r)
norm.cdf(r)
norm.logcdf(r)
r = np.random.randn(10000, 2)
plt.scatter(r[:,0], r[:,1])
plt.show()
r[:,1] = 5 * r[:,1] + 2
plt.scatter(r[:,0], r[:,1])
plt.show()
plt.axis('equal')
plt.show()
plt.scatter(r[:,0], r[:,1])
plt.axis('equal')
plt.show()
