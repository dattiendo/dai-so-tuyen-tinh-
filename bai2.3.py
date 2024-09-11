import numpy as np
A = np.array([[1, 1, 1], [2, 3, 5], [4, 0, 5]])
B = np.array([6, -4, 27])
X = np.linalg.solve(A, B)
print(X)
