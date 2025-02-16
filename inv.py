import numpy as np

A = np.array([[3, 5, 8],
            [9, 3, 7],
            [3, 9, 7]])

if np.linalg.det(A) == 0:
    print("Determinan A = 0, sehingga tidak memiliki invers")
else:
    hasil = np.linalg.inv(A)

print(hasil)