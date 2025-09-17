import numpy as np

#Ejercicio1
X = np.array([1,2,5])
W = np.array([[3, 1, 4],
             [2, 7, 5]])
B = np.array([1, 2])

print(f'\nX(W^T) + B = {(X@W.T) + B}\n\n')

#Ejercicio2
X = np.array([
    [1, 2],
    [2, 3],
    [4, 1]
])
W = np.array([
    [2, 5],
    [4, 3],
    [2, 1]
])
B = np.array([2, 3, 2])

print(f'Ejercicio 2\n\nXW + B =\n{(X@W.T) + B}\n\n')