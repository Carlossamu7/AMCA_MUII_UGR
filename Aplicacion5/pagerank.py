"""
Máster Universitario en Ingeniería Informática UGR
Aplicaciones de Matemática Computacional Avanzada (2020-2021)
Carlos Santiago Sánchez Muñoz
"""

import numpy as np

""" Método de las potencias.
- A: matriz.
- x: vector.
- iters: número de iteraciones.
"""
def metodo_potencias(A, x, iters):
    for _ in range(iters-1):
        x = A.dot(x)

    x_new = A.dot(x)
    return(x_new, x)

""" Método de las potencias normalizado.
- A: matriz.
- x: vector.
- iters: número de iteraciones.
"""
def metodo_potencias_normalizado(A, x, iters):
    for _ in range(iters-2):
        x = normaliza(A.dot(x))
    x = A.dot(x)
    x_new = A.dot(normaliza(x))
    return(x_new, x)

""" Normaliza el vector usando la norma infinito.
- x: vector a normalizar.
"""
def normaliza(x):
    return x / np.linalg.norm(x, np.inf)

print("Ejercicio Page Rank")
print("\nMatriz S")
S = np.array([
    [0, 1/3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1/3, 0, 1/3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1/3, 0, 1/2, 0, 0, 0, 0, 0, 1/3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1/3, 0, 0, 0, 0, 1/3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    [1/3, 1/3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1/3, 0, 0, 0, 0, 0, 0, 0, 1/6, 0, 0, 0, 0, 0, 0],
    [0, 0, 1/2, 1/3, 0, 0, 1/3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1/6, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1/3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/3],

    [0, 0, 0, 0, 0, 1/3, 1/3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1/3, 0, 0, 0, 1, 0, 1/2, 1/6, 0, 1/2, 1/3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1/3, 1/2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/6, 0, 0, 0, 0, 0, 1/3],

    [1/3, 0, 0, 0, 0, 1/3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/6, 0, 0, 1/3, 0, 0, 1/3],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1/6, 0, 0, 0, 1/2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
])

alpha=0.85

# Dando igual importancia a todos los links de aquellas páginas que no tienen link
S[:,4] = 1/20
S[:,14] = 1/20

print(S)

# Sumando por columnas para verificar que es correcta
print("\nSuma por columnas:")
print(np.sum(S, axis=0))

""" Devuelve la matriz de google
- S: matriz sacada del grafo.
- alpha: valor entre 0 y 1.
"""
def google_matrix(S, alpha):
    n =len(S)
    if(n!=len(S[1]) or alpha<0 or alpha>1):
        exit()
    ones = 1/n * np.ones((n,n))
    return(alpha*S + (1-alpha)*ones)

# Matriz de Google
G = google_matrix(S, alpha)

print("\nMatriz de Google")
print(G)

x = np.ones(len(S))
print(x)

(x_new, _) = metodo_potencias_normalizado(G, x, 10)
print("\nMétodo de las potencias normalizado a la matriz de Google")
print(x_new)
print("\nEl mayor valor lo tiene la página 13")
