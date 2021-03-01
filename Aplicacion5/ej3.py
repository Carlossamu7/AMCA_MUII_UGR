"""
Máster Universitario en Ingeniería Informática UGR
Aplicaciones de Matemática Computacional Avanzada (2020-2021)
Carlos Santiago Sánchez Muñoz
"""

import numpy as np

# Función que decodifica de CRS a la matriz dispersa
def CRS_to_SparseMatrix(AA, JA, IA):
    # Dimensiones de la matriz
    n = len(IA)-1
    # Matriz de ceros con dicha dimensión
    matrix = np.zeros((n,n))
    # Inicializo el contador
    cont = 0

    # Recorro la lista IA
    for i in range(n):
        notnull = IA[i+1] - IA[i]
        # Recorro las listas JA y AA
        for j in range(notnull):
            matrix[i, JA[cont+j]-1] = AA[cont+j]
        # Actualizo el contador
        cont = cont + notnull

    # Devuelvo la matriz
    return matrix

# Creo las listas
AA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
JA = [1, 4, 1, 2, 4, 1, 3, 4, 5, 3, 4, 5]
IA = [1, 3, 6, 10, 12, 13]

# Creo las listas
#AA = [8, 4, 1, 3, 2, 1, 7, 9, 3, 1, 5]
#JA = [1, 2, 3, 4, 1, 3, 5, 2, 3, 6, 6]
#IA = [1, 3, 5, 8,11,12]

sparse_matrix = CRS_to_SparseMatrix(AA, JA, IA)
print(sparse_matrix)
