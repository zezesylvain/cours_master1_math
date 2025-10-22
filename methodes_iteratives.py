import numpy as np


def jacobi_iteration(A: np.ndarray, b: np.ndarray, x_old: np.ndarray) -> np.ndarray:
    """
    Exécute une seule itération du schéma de Jacobi.

    Données: A, b, x_old
    A: Matrice du système (numpy array)
    b: Vecteur du second membre (numpy array)
    x_old: Vecteur solution de l'itération précédente (numpy array)

    Retourne: x_new (Vecteur solution de la nouvelle itération)
    """

    # n = dimension du problème
    n = A.shape[0]

    # x_new = 0(n) (Initialisation du nouveau vecteur solution)
    x_new = np.zeros(n)

    # Pour i allant de 0 à n-1 (0-based indexing en Python)
    for i in range(n):

        # s = 0 (Initialisation de la somme)
        s = 0

        # Pour j allant de 0 à n-1 tel que j ≠ i faire
        for j in range(n):
            if i != j:
                # s = s + a_ij * x_j_old
                s += A[i, j] * x_old[j]

        # Vérification pour éviter la division par zéro (nécessaire pour Jacobi)
        if A[i, i] == 0:
            raise ValueError(f"L'élément diagonal A[{i},{i}] est nul. L'itération de Jacobi ne peut pas procéder.")

        # x_i_new = (1/a_ii) * (b_i - s)
        # Ceci est la formule de mise à jour de Jacobi.
        x_new[i] = (b[i] - s) / A[i, i]

    # Retourner x_new
    return x_new


# --- Exemple d'utilisation ---

# Définition du système A x = b
A_example = np.array([
    [10., -1., 2., 0.],
    [-1., 11., -1., 3.],
    [2., -1., 10., -1.],
    [0., 3., -1., 8.]
])

b_example = np.array([6., 25., -11., 15.])

# x_old (Initialisation de la première itération, souvent un vecteur nul)
x_old_example = np.zeros_like(b_example)

print(f"Vecteur initial x_old:\n{x_old_example}")

# Exécution d'une itération
x_new_example = jacobi_iteration(A_example, b_example, x_old_example)

print("\n------------------------------")
print(f"Vecteur solution après 1 itération (x_new):\n{x_new_example}")

x_new_example1 = jacobi_iteration(A_example, b_example, x_new_example)

print("\n------------------------------")
print(f"Vecteur solution après 1 itération (x_new):\n{x_new_example1}")