# Spline Quadratique Avec SymPy

** 6 045  tokens **

User

![Capture d’écran 2025-10-29 à 10.02.20.png](blob:https://aistudio.google.com/a9018c49-2825-4eb9-b5e5-7c6f0d3e6a34)

Model

![Thinking](https://www.gstatic.com/aistudio/watermark/watermark.png) Thoughts **(experimental)** Auto

Expand to view model thoughts

chevron\_right

**C'est un excellent algorithme pour l'implémentation d'une fonction d'interpolation par splines quadratiques.**

**Voici la traduction de cet algorithme en un programme Python complet. J'utilise la librairie **sympy** pour la définition symbolique de la fonction **

```
        f
    
```

et de sa dérivée, et **numpy** et **matplotlib** pour les calculs numériques et la visualisation.

### Programme Python : Algorithme de Spline Quadratique

** code **Python

```
    import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# --- 2. Definition des variables (et des fonctions) ---

# 1. Définition symbolique de la variable et de la fonction f(x)
x = sp.Symbol('x')

# Exemple de fonction f(x) que vous pouvez modifier
# f(x) = sin(x) * exp(-x/5)
f_sym = sp.sin(x) * sp.exp(-x/5)

# Calcul symbolique de la dérivée f'(x)
f_prime_sym = sp.diff(f_sym, x)

# Création de fonctions numériques (lambdify) pour l'évaluation rapide
f_num = sp.lambdify(x, f_sym, 'numpy')
f_prime_num = sp.lambdify(x, f_prime_sym, 'numpy')

# Paramètres de l'interpolation
x_min, x_max = 0, 10
N_intervalles = 4  # Nombre d'intervalles (n dans l'algo, il y aura N_intervalles + 1 points)
nb = 20            # 2.5. nb: nombre de points par intervalle pour l'évaluation (nb+1 total)
epsilon = 1e-15    # 7. Epsilon pour le calcul de l'erreur

# Points de l'interpolation (noeuds)
x_knots = np.linspace(x_min, x_max, N_intervalles + 1)
n = N_intervalles # n = nombre d'intervalles [x_i, x_{i+1}]

# 1. Calcul des y_i
y_knots = f_num(x_knots)

# 2.4. Calcul de z0 = f'(x0) (Condition de bord)
# z[i] représente la dérivée S'(x_i)
z = np.zeros(n + 1) # z_0 à z_n
z[0] = f_prime_num(x_knots[0])

# Initialisation des listes de résultats
points = []          # 2.1. l'ensemble des points à évaluer
sol_approchee = []   # 2.2. Résultats de S(x)
# sol_exacte sera calculé plus tard (2.3.)

# --- Calcul des z_i suivants et définition des Splines ---

# On utilise la relation de récurrence pour la spline quadratique:
# z_{i+1} = -z_i + 2 * (y_{i+1} - y_i) / h_i

for i in range(n):
    x_i, x_i_plus_1 = x_knots[i], x_knots[i+1]
    y_i, y_i_plus_1 = y_knots[i], y_knots[i+1]
    h_i = x_i_plus_1 - x_i

    # 3.1. Calcul de z_{i+1}
    z[i+1] = -z[i] + 2 * (y_i_plus_1 - y_i) / h_i
    z_i, z_i_plus_1 = z[i], z[i+1]

    # 3.2. Calcul de S(x) (Définition symbolique de la spline S_i(x) avec sympy)
    # S_i(x) = y_i + z_i*(x - x_i) + (z_{i+1} - z_i)/(2*h_i) * (x - x_i)^2
    S_i_sym = y_i + z_i * (x - x_i) + (z_i_plus_1 - z_i) / (2 * h_i) * (x - x_i)**2
  
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

# Affichage des valeurs z_i (dérivées aux noeuds) pour vérification
print("\nValeurs des dérivées z_i = S'(x_i) aux noeuds:")
print(z)
  
```

### Explication de l'utilisation de **sympy** :

* **Définition des fonctions (**

  <pre _ngcontent-ng-c453147825=""><strong _ngcontent-ng-c4139270029="" class="ng-star-inserted">        <code _ngcontent-ng-c453147825="" class="rendered"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>f</mi></mrow></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord mathnormal">f</span></span></span></span></code>
        </strong></pre>

  ** et

  ```
          f′

  ```

  )** :

  * **x = sp.Symbol('x')** : Définit **x** comme une variable symbolique.
  * **f\_sym = sp.sin(x) \* sp.exp(-x/5)** : Définit la fonction

    ```
            f

    ```

    symboliquement.
  * **f\_prime\_sym = sp.diff(f\_sym, x)** : Calcule la dérivée

    ```
            f′

    ```

    symboliquement.
* **Passage au numérique (**lambdify**)** :

  * **f\_num = sp.lambdify(x, f\_sym, 'numpy')** : Convertit l'expression symbolique **f\_sym** en une fonction qui utilise les fonctions de **numpy**. Cela permet d'évaluer la fonction rapidement sur des tableaux de points (**x\_knots** ou **points\_np**). C'est crucial pour les calculs et le tracé.
* **Définition de la Spline **

  <pre _ngcontent-ng-c453147825=""><strong _ngcontent-ng-c4139270029="" class="ng-star-inserted">        <code _ngcontent-ng-c453147825="" class="rendered"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>S</mi><mi>i</mi></msub><mo stretchy="false">(</mo><mi>x</mi><mo stretchy="false">)</mo></mrow></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord"><span class="mord mathnormal">S</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span class=""><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s"></span></span><span class="vlist-r"><span class="vlist"><span class=""></span></span></span></span></span></span><span class="mopen">(</span><span class="mord mathnormal">x</span><span class="mclose">)</span></span></span></span></code>
        </strong></pre>

  ** (dans la boucle)** :

  * **S\_i\_sym = ...** : La définition de la spline

    ```
            Si(x)

    ```

    est écrite directement en utilisant la variable symbolique **x** et les coefficients numériques calculés (

    ```
            yi,zi,zi+1,hi

    ```

    ).
  * **S\_i\_num = sp.lambdify(x, S\_i\_sym, 'numpy')** : Chaque spline est transformée en une fonction numérique pour être évaluée sur les points de subdivision

    ```
            Xi

    ```

    .

**Formule de Spline Quadratique utilisée :**
La spline

```
        Si(x)
    
```

sur l'intervalle

```
        [xi,xi+1]
    
```

est définie par :

```
        Si(x)=yi+zi(x−xi)+2hizi+1−zi(x−xi)2
    
```

où

```
        zi=Si′(xi)
    
```

et

```
        zi+1=Si′(xi+1)
    
```

.

**Formule de Récurrence pour les **

<pre _ngcontent-ng-c453147825=""><strong _ngcontent-ng-c4139270029="" class="ng-star-inserted">        <code _ngcontent-ng-c453147825="" class="rendered"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>z</mi><mi>i</mi></msub></mrow></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"></span><span class="mord"><span class="mord mathnormal">z</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"><span class=""><span class="pstrut"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathnormal mtight">i</span></span></span></span><span class="vlist-s"></span></span><span class="vlist-r"><span class="vlist"><span class=""></span></span></span></span></span></span></span></span></span></code>
      </strong></pre>

** (Step 3.1) :**

```
        zi+1=−zi+2hiyi+1−yi
    
```

** 28,4s **

Use Arrow Up and Arrow Down to select a turn, Enter to jump to it, and Escape to return to the chat.

[ ]

Response ready.
