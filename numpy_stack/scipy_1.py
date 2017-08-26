# coding: utf-8
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
