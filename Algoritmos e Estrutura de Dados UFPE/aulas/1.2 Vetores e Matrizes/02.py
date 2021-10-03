import numpy as np
'''v = np.zeros(5, int)
v[0] = 5
v[-2] = 3
print(v)

mat = np.zeros((4,3), float)
mat[0][1] = 2.0
print(mat)'''

mat1 = np.zeros((6,6), int)
aux = 0
for i in range(6):
    mat1[i] = np.arange(aux, aux+6)
    aux += 10
print(mat1)
print(mat1[0,3:5])