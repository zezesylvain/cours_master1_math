
from systeme_lineaire import *

# --- Exemple d'utilisation ---

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