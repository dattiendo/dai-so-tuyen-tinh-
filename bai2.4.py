import numpy as np
A = np.array([[2, -3, 1], [4, -6, 2], [-2, 3, -1]])
B = np.array([5, 10, -3])
det_A = np.linalg.det(A)
if det_A != 0:
    x = np.linalg.solve(A, B)
    print('hệ phương trình có nghiệm duy nhất')
    print(x)
else:
    print('hệ phương trình vô nghiệm hoặc có vô số nghiệm')
