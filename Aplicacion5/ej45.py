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
    for i in range(iters-1):
        x = A.dot(x)

    x_new = A.dot(x)
    return(x_new, x)

""" Método de las potencias normalizado.
- A: matriz.
- x: vector.
- iters: número de iteraciones.
"""
def metodo_potencias_normalizado(A, x, iters):
    for i in range(iters-1):
        x = normaliza(A.dot(x))

    x_new = A.dot(x)
    return(x_new, x)

""" Normaliza el vector usando la norma infinito.
- x: vector a normalizar.
"""
def normaliza(x):
    return x / np.linalg.norm(x, np.inf)

""" Imprime la solución
- x_ant: vector de la penúltima iteración.
- x_new: vector de la última iteración.
- title: título a imprimir.
"""
def print_sol(x_ant, x_new, title):
    print(title)
    print("Penúltima iteración: {}".format(x_ant))
    print("Última iteración: {}".format(x_new))
    print("Última iteración normalizado: {}".format(normaliza(x_new)))
    print("Valor propio: {}".format(x_new[0]/x_ant[0]))
    print()

A = np.array([[3, 1, 1],
               [1, 3, 1],
               [1, 1, 3]])

x = np.array([1,0,0])

# Ejecuto el método de las potencias
(x_new, x_ant) = metodo_potencias(A, x, 10)
print_sol(x_ant, x_new, "Método de las potencias")

# Ejecuto el método de las potencias normalizado
(x_new, x_ant) = metodo_potencias_normalizado(A, x, 10)
print_sol(x_ant, x_new, "Método de las potencias normalizado")
