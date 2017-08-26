# coding: utf-8
import numpy as np
A = np.array([[1,2],[3,4]])
b = np.array([3,4])
b = np.array([1,2])
x = np.linalg.inv(A).dot(b)
x
x = np.linalg.solve(A, b)
x
# always use solve(), never use the inverse method
# solve() is more efficient and more accurate
