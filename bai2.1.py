import numpy as np
A = np.array([[2, 3, 1], [4, 1, 5], [3, 2, 4]])
B = np.array([1, 2, 3])
A_inv = np.linalg.inv(A)
X = np.dot(A_inv, B)
print(X)

