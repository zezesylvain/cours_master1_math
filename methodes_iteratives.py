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





def relaxation_step(A, b, x_old, omega = 1):
    """
    Exécute une seule étape de l'algorithme de relaxation.

    Args:
        A (np.array): La matrice des coefficients.
        b (np.array): Le vecteur du second membre.
        x_old (np.array): Le vecteur de la solution de l'itération précédente.
        omega (float): Le facteur de relaxation.

    Returns:
        np.array: Le vecteur de la nouvelle solution calculée (x_new).
    """

    n = A.shape[0] # Dimension du problème
    x_new = np.copy(x_old) # Initialise x_new avec les valeurs de x_old

    # Pour i allant de 0 à n-1 (en Python, les indices commencent à 0)
    for i in range(n):
        # S1 = 0
        S1 = 0.0
        # Pour j allant de 0 à i-1 Faire
        for j in range(i):
            S1 += A[i, j] * x_new[j] # Utilise x_new pour les j < i (car ils sont déjà mis à jour)
        # Fin Pour

        # S2 = 0
        S2 = 0.0
        # Pour j allant de i+1 à n-1 Faire
        for j in range(i + 1, n):
            S2 += A[i, j] * x_old[j] # Utilise x_old pour les j > i (car x_new n'est pas encore mis à jour pour ces j)
        # Fin Pour

        # Vérification pour éviter la division par zéro
        if A[i, i] == 0:
            raise ValueError(f"L'élément diagonal A[{i},{i}] est nul. Impossible de diviser par zéro.")

        # x_i_new = (1 / a_i,i) * (omega * b_i + (1 - omega) * a_i,i * x_i_old - omega * (S1 + S2))
        x_new[i] = (1 / A[i, i]) * (omega * b[i] + (1 - omega) * A[i, i] * x_old[i] - omega * (S1 + S2))
    # Fin Pour (de la boucle sur i)

    return x_new

def gauss_seidel_step(A, b, x_old):
    return  relaxation_step(A, b, x_old)


"""""
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

"""