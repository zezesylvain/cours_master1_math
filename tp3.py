
#import numpy as np
from systeme_lineaire import *

# Définition du système A x = b
A = np.array([
    [10., -1., 2., 0.],
    [-1., 11., -1., 3.],
    [2., -1., 10., -1.],
    [0., 3., -1., 8.]
])

b = np.array([6., 25., -11., 15.])
epsilon = 1e-8
x, nb, valeur = resolution_par_methode_iterative_amelioree(A, b, epsilon, None, 'relaxation', 2.125)
if valeur:
    print(f" la solution est {x}")
    print(f"Le nombre d'iterations pour arriver a la solution est {nb}")
else:
    print(f" La convergence n'a pas ete atteinte avec {nb} iterations")


"""
Pour Jacobi
nb = 24 pour 1e-8

Pour Gauss Seidel
nb = 10 pour 1e-8
Pour Relaxation
nb = 32 pour 1e-8 omega = 1.5
nb = 39 pour 1e-8 omega = 0.5
nb = 90 pour 1e-8 omega = 0.25
nb = 186 pour 1e-8 omega = 0.125
nb = 21 pour 1e-8 omega = 0.725
nb = 14 pour 1e-8 omega = 0.925
nb = 12 pour 1e-8 omega = 1.125

omega de 0 a 2 par pas de 0.001
tracer le nombre d'iterations en fonction de omega
"""