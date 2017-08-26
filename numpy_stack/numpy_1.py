# coding: utf-8
get_ipython().magic(u'load numpy_exc.py')
# %load numpy_exc.py
import numpy as np
A = np.array([1,2,3])
2 * A
A + A
for e in A:
    print e
    
A ** 2
# most functions are element-wise
np.sqrt(A)
np.log(A)
np.exp(A)
# np.array is vector
# dot product
a = np.array([1,2])
b = np.array([2,1])
a * b
np.sum(a*b)
(a*b).sum()
np.dot(a, b)
a.dot(b)
b.dot(a)
amag = np.sqrt( (a*a).sum() )
amag
amag = np.linalg.norm(a)
amag
cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
cosangle
angle = np.arccos(cosangle)
angle
