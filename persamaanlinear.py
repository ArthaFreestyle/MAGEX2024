import numpy as np

A = np.array([[0,1,0],[0,0,1],[4,-17,8]])

eigenvalue = np.linalg.eigvals(A)
print(eigenvalue)