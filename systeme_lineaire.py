import numpy as np
from scipy.linalg import lu

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



# --- Exemple d'utilisation ---
if __name__ == "__main__":
    # 1. Matrice A (triangulaire inférieure)
    A = np.array([
        [2, 0, 0],
        [1, 3, 0],
        [4, 2, 5]
    ], dtype=float)

    # 2. Vecteur colonne b
    b = np.array([6, 10, 27], dtype=float)

    print("Matrice A :")
    print(A)
    print("\nVecteur b :")
    print(b)

    try:
        x = systeme_triangulaire_inferieur(A, b)
        print("\nLa solution x est :")
        print(x)
        # Vérification: Ax = b
        print("\nVérification (Ax) :")
        print(np.dot(A, x))
    except ValueError as e:
        print(f"\nErreur : {e}")

    print("\n--- Deuxième exemple ---")
    A2 = np.array([
        [1, 0, 0, 0],
        [2, 1, 0, 0],
        [3, 2, 1, 0],
        [4, 3, 2, 1]
    ], dtype=float)
    b2 = np.array([1, 4, 10, 20], dtype=float)

    print("Matrice A2 :")
    print(A2)
    print("\nVecteur b2 :")
    print(b2)

    try:
        x2 = systeme_triangulaire_inferieur(A2, b2)
        print("\nLa solution x2 est :")
        print(x2)
        print("\nVérification (A2x2) :")
        print(np.dot(A2, x2))
    except ValueError as e:
        print(f"\nErreur : {e}")

    print("\n--- Exemple avec terme diagonal nul ---")
    A_singular = np.array([
        [1, 0],
        [2, 0]
    ], dtype=float)
    b_singular = np.array([3, 5], dtype=float)
    try:
        x_singular = systeme_triangulaire_inferieur(A_singular, b_singular)
        print("\nLa solution x_singular est :")
        print(x_singular)
    except ValueError as e:
        print(f"\nErreur : {e}")