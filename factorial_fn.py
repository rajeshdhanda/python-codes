import numpy as np
A = np.array([])
for j in range(2 ,100):
    for i in range(2 ,j):
        if j% i == 0:
            j += 1
            continue
    else:
        A = np.append(A, j)
        j += 1
        continue

print(A)