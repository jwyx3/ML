# coding: utf-8
import numpy as np
# matrix multiplication, interdimension must match
# * asterisk
# A * B is element-wise multiplication
# C = A.dot(B) is matrix multiplication
# A * B: both arrays must be same size
# show matrix operations
A = np.array([[1,2],[3,4]])
Ainv = np.linalg.inv(A)
Ainv
Ainv.dot(A)
A.dot(Ainv)
# matrix muliplication of A and Ainv is Identical matrix
np.linalg.det(A)
np.diag(A)
np.diag([1,2])
# Outer product
# Inner product = dot product
# Outer product: C(i,j) = A(i)B(j)
# Inner product: C = sum over i {A(i)B(i)}
a = np.array([1,2])
b = np.array([3,4])
np.outer(a, b)
np.inner(a, b)
a.dot(b)
np.diag(A).sum()
np.trace(A)
X = np.random.randn(100, 3)
cov = np.cov(X)
cov.shape
cov
cov = np.cov(X.T)
cov
# eigenvalues, eigenvectors = np.eig(C)
np.linalg.eigh(cov)
np.linalg.eig(cov)
