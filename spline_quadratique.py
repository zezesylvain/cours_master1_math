import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
#from sympy import sin, cos, symbols, exp, lambdify, diff

# --- 2. Definition des variables (et des fonctions) ---

# 1. Définition symbolique de la variable et de la fonction f(x)
x = sp.Symbol('x')

# Exemple de fonction f(x) que vous pouvez modifier
# f(x) = sin(x) * exp(-x/5)
f_sym = sp.sin(x) * sp.exp(-x / 5)

# Calcul symbolique de la dérivée f'(x)
f_prime_sym = sp.diff(f_sym, x)

# Création de fonctions numériques (lambdify) pour l'évaluation rapide
f_num = sp.lambdify(x, f_sym, 'numpy')
f_prime_num = sp.lambdify(x, f_prime_sym, 'numpy')

# Paramètres de l'interpolation
x_min, x_max = 0, 10
N_intervalles = 100  # Nombre d'intervalles (n dans l'algo, il y aura N_intervalles + 1 points)
nb = 20  # 2.5. nb: nombre de points par intervalle pour l'évaluation (nb+1 total)
epsilon = 1e-15  # 7. Epsilon pour le calcul de l'erreur

# Points de l'interpolation (noeuds)
x_knots = np.linspace(x_min, x_max, N_intervalles + 1)
n = N_intervalles  # n = nombre d'intervalles [x_i, x_{i+1}]

# 1. Calcul des y_i
y_knots = f_num(x_knots)

# 2.4. Calcul de z0 = f'(x0) (Condition de bord)
# z[i] représente la dérivée S'(x_i)
z = np.zeros(n + 1)  # z_0 à z_n
z[0] = f_prime_num(x_knots[0])

# Initialisation des listes de résultats
points = []  # 2.1. l'ensemble des points à évaluer
sol_approchee = []  # 2.2. Résultats de S(x)
# sol_exacte sera calculé plus tard (2.3.)

# --- Calcul des z_i suivants et définition des Splines ---

# On utilise la relation de récurrence pour la spline quadratique:
# z_{i+1} = -z_i + 2 * (y_{i+1} - y_i) / h_i

for i in range(n):
    x_i, x_i_plus_1 = x_knots[i], x_knots[i + 1]
    y_i, y_i_plus_1 = y_knots[i], y_knots[i + 1]
    h_i = x_i_plus_1 - x_i

    # 3.1. Calcul de z_{i+1}
    z[i + 1] = -z[i] + 2 * (y_i_plus_1 - y_i) / h_i
    z_i, z_i_plus_1 = z[i], z[i + 1]

    # 3.2. Calcul de S(x) (Définition symbolique de la spline S_i(x) avec sympy)
    # S_i(x) = y_i + z_i*(x - x_i) + (z_{i+1} - z_i)/(2*h_i) * (x - x_i)^2
    S_i_sym = y_i + z_i * (x - x_i) + (z_i_plus_1 - z_i) / (2 * h_i) * (x - x_i) ** 2

    # On la transforme en fonction numérique pour l'évaluation
    S_i_num = sp.lambdify(x, S_i_sym, 'numpy')

    # 3.3. Subdivision X_i de l'intervalle [x_i, x_{i+1}] en nb+1 points
    X_i = np.linspace(x_i, x_i_plus_1, num=nb + 1)

    # 3.4. On ajoute la subdivision X_i dans Points sauf le dernier point (x_{i+1})
    points.extend(X_i[:-1])

    # 3.5. Évaluation de S aux points et ajout dans sol_approchee
    # Les points X_i[:-1] sont ceux ajoutés dans la liste 'points'
    sol_approchee.extend(S_i_num(X_i[:-1]))

# --- Finalisation de l'évaluation ---

# 4. On ajoute x_n dans points
points.append(x_knots[-1])

# 5. On calcule S(x_n) = S_{n-1}(x_n) et on l'ajoute dans sol_approchee
# Pour une spline, S_{n-1}(x_n) doit être égal à y_n
sol_approchee.append(y_knots[-1])

# Conversion en tableaux numpy pour les calculs d'erreurs
points_np = np.array(points)
sol_approchee_np = np.array(sol_approchee)

# 6. On évalue f en tous les éléments de points pour obtenir sol_exacte
sol_exacte_np = f_num(points_np)

# 7. On calcule l'erreur Erreur = log(|sol_exacte - sol_approchee| + epsilon)
Erreur = np.log10(np.abs(sol_exacte_np - sol_approchee_np) + epsilon)
# Affichage des valeurs z_i (dérivées aux noeuds) pour vérification
print("\nValeurs des dérivées z_i = S'(x_i) aux noeuds:")
print(z)
# --- 8. On trace les graphiques ---

plt.figure(figsize=(12, 6))

# 8.1. sol_exacte et sol_approchee sur le meme graphique
plt.subplot(1, 2, 1)
plt.plot(points_np, sol_exacte_np, label=r'$f(x)$ (sol_exacte)', color='green')
plt.plot(points_np, sol_approchee_np, label=r'$S(x)$ (sol_approchee)', linestyle='--', color='red')
plt.scatter(x_knots, y_knots, label='Noeuds ($x_i, y_i$)', color='blue', zorder=5)
plt.title(f"Approximation par Spline Quadratique ({N_intervalles} intervalles)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

# 8.2. Erreur sur un autre graphique
plt.subplot(1, 2, 2)
plt.plot(points_np, Erreur, color='orange')
plt.title(r"Erreur $\log_{10}(|f(x) - S(x)| + \epsilon)$")
plt.xlabel("x")
plt.ylabel(r"$\log_{10}$ Erreur")
plt.grid(True, linestyle=':', alpha=0.6)
plt.axhline(np.log10(epsilon), color='r', linestyle=':', label=r'$\log_{10}(\epsilon)$')
plt.legend()

plt.tight_layout()
plt.show()


