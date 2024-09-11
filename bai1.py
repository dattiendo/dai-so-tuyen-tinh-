import numpy as np
#1
A = np.array([[3, 2, 4], [4, 8, 7], [7, 8, 10]])
B = np.array([[9, 7, 8], [6, 4, 5], [3, 2, 1]])
#2
print(A + B)
#3
print(A - B)
#4
a = np.dot(A, B)
print(a)
#5
print(A * B)
#6
detA = np.linalg.det(A)
print(detA) 
#7
invA = np.linalg.inv(A)
print(invA)
#8
tA = A.T
print (tA)
#9
mpA = np.linalg.pinv(A)
print(mpA)
#10
frA = np.linalg.norm(A)
print(frA)
#11
L1_n = np.linalg.norm(A, ord=1, axis=1)
L2_n = np.linalg.norm(A, ord=2, axis=1)
print(L1_n)
print(L2_n)
#12
m2x2 = A[:2, :2]
print(m2x2)
#13
sm_A = 2 * A
print (sm_A)
#14
A_T_A = np.dot(A.T, A)
print(A_T_A)
#15
trace_A = np.trace(A)
print(trace_A)
#16
eigenvalues_A, eigenvectors_A = np.linalg.eig(A)
print(eigenvalues_A)
print(eigenvectors_A)
#18
C = np.array([[1, 1, 1],[1, 1, 1],[1, 1, 1]])
print(C + A)
#21
D = np.array([[5, 3, 6, 7],[5, 6, 7, 2],[7, 8, 9, 5], [4, 3, 2, 5]])
print(D)