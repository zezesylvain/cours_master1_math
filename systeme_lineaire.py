#import numpy as np
from scipy.linalg import lu
from methodes_iteratives import *

def systeme_triangulaire_inferieur(A, b):
    """
    Résout un système linéaire Ax = b où A est une matrice triangulaire inférieure.

    Args:
        A (np.array): Matrice triangulaire inférieure de taille n x n.
        b (np.array): Vecteur colonne de taille n x 1.

    Returns:
        np.array: Le vecteur solution x de taille n x 1.

    Raises:
        ValueError: Si A n'est pas une matrice carrée ou si les dimensions de A et b ne correspondent pas.
    """
    n = A.shape[0]

    # Vérifications de la taille de la matrice et du vecteur
    if A.shape[1] != n:
        raise ValueError("La matrice A doit être carrée.")
    if len(b) != n:
        raise ValueError("Les dimensions de la matrice A et du vecteur b ne correspondent pas.")

    x = np.zeros(n)

    for i in range(n):
        sum_val = 0
        for j in range(i):
            sum_val += A[i, j] * x[j]

        # Vérifier si le terme diagonal est nul pour éviter la division par zéro
        if A[i, i] == 0:
            raise ValueError("La matrice A est singulière (terme diagonal nul), le système ne peut pas être résolu par substitution avant.")

        x[i] = (b[i] - sum_val) / A[i, i]

    return x


def systeme_triangulaire_superieur(A, b):
    """
       Résout un système linéaire Ax = b où A est une matrice triangulaire supérieure.

       Args:
           A (np.array): Matrice triangulaire supérieure de taille n x n.
           b (np.array): Vecteur colonne de taille n x 1.

       Returns:
           np.array: Le vecteur solution x de taille n x 1.

       Raises:
           ValueError: Si A n'est pas une matrice carrée ou si les dimensions de A et b ne correspondent pas.
       """
    n = A.shape[0]

    # Vérifications de la taille de la matrice et du vecteur
    if A.shape[1] != n:
        raise ValueError("La matrice A doit être carrée.")
    if len(b) != n:
        raise ValueError("Les dimensions de la matrice A et du vecteur b ne correspondent pas.")

    x = np.zeros(n)

    # L'itération commence par la dernière ligne (n-1) et remonte jusqu'à 0
    for i in range(n - 1, -1, -1):  # i va de n-1, n-2, ..., 0
        sum_val = 0
        # La somme va de j = i+1 jusqu'à n-1
        for j in range(i + 1, n):
            sum_val += A[i, j] * x[j]

        # Vérifier si le terme diagonal est nul pour éviter la division par zéro
        if A[i, i] == 0:
            raise ValueError(
                "La matrice A est singulière (terme diagonal nul), le système ne peut pas être résolu par substitution arrière.")

        x[i] = (b[i] - sum_val) / A[i, i]

    return x


def resolution_systeme_lineaire_lu(A, b):
    """
       Résout un système linéaire Ax = b où A est une matrice carre quelconque.

       Args:
           A (np.array): Matrice  de taille n x n.
           b (np.array): Vecteur colonne de taille n x 1.

       Returns:
           np.array: Le vecteur solution x de taille n x 1.

       Raises:
           ValueError: Si A n'est pas une matrice carrée ou si les dimensions de A et b ne correspondent pas.
    """
    n = A.shape[0]

    # Vérifications de la taille de la matrice et du vecteur
    if A.shape[1] != n:
        raise ValueError("La matrice A doit être carrée.")
    if len(b) != n:
        raise ValueError("Les dimensions de la matrice A et du vecteur b ne correspondent pas.")

    x = np.zeros(n)
    P, L, U = lu(A)
    pb = P @ b
    y = systeme_triangulaire_inferieur(L, pb)
    x = systeme_triangulaire_superieur(U, y)
    return x


# Supposons que jacobi_iteration est définie comme précédemment

def resolution_par_methode_iterative_amelioree(A, b, precision, x0=None, methode = 'jacobi', omega = 1, nb_it_max=1000):
    """
        Resoud un systeme lineaire par le schéma de Jacobi.

        Données: A, b, precision, nb_it_max, x0
        A: Matrice du système (numpy array)
        b: Vecteur du second membre (numpy array)
        precision: Precision, un scalaire positif tres petit (Float)
        nb_it_max: Entier, nombre d'iteration maximal a ne pas depasser (Integer)
        x0: Vecteur solution initiale (numpy array)

        Retourne:  x, nb_it, bool
         x: Vecteur solution de la nouvelle itération (numpy array)
         nb_it: Nombre d'iterations necessaire a la resolution (Integer)
         bool: Variable qui indique s'il y a eu convergence (Boolean)
        """

    n = A.shape[0]

    # Vérifications de la taille de la matrice et du vecteur
    if A.shape[1] != n:
        raise ValueError("La matrice A doit être carrée.")
    if len(b) != n:
        raise ValueError("Les dimensions de la matrice A et du vecteur b ne correspondent pas.")

    if x0 is None:
        # Assurer que la dimension est correcte (colonnes de A)
        x_old = np.zeros(A.shape[1])
    else:
        if x0.shape == b.shape:
            x_old = np.copy(x0)
        else:
            x_old = np.zeros(A.shape[1])

    nb_it = 0

    # x_new doit être initialisé pour la boucle, par exemple en copiant x_old
    x_new = np.copy(x_old)

    # Critère d'arrêt initial (grande valeur pour entrer dans la boucle)
    norm_diff = np.inf

    # Boucle tant que l'écart entre les itérations est trop grand
    # ET que le nombre max d'itérations n'est pas atteint
    while norm_diff > precision and nb_it < nb_it_max:

        # 1. Calculer la nouvelle solution en fonction de la methode indiquee
        if methode == 'gauss':
            x_new = gauss_seidel_step(A, b, x_old)
        elif methode == 'relaxation':
            x_new = relaxation_step(A, b, x_old, omega)
        else:
            x_new = jacobi_iteration(A, b, x_old)

        # 2. Calculer le critère d'arrêt : ||x_new - x_old||
        norm_diff = np.linalg.norm(x_new - x_old)

        # 3. Mettre à jour pour la prochaine itération
        x_old = np.copy(x_new)
        nb_it += 1

    # Le vecteur solution final est x_new (ou x_old après la dernière mise à jour)
    x = x_old

    if nb_it < nb_it_max:
        # Convergence atteinte
        return x, nb_it, True
    else:
        # Nombre max d'itérations atteint
        return x, nb_it, False


