# SymPy Pour les Mathématiques Universitaires

** 2 411  tokens **

Model

![Thinking](https://www.gstatic.com/aistudio/watermark/watermark.png) Thoughts **(experimental)** Auto

Expand to view model thoughts

chevron\_right

**SymPy : Calcul Symbolique pour l'Étudiant en Licence de Mathématiques**

---

**SymPy est une bibliothèque Python libre et open-source dédiée au **calcul symbolique** (ou formel). Elle se présente comme un **Système d'Algèbre Informatique (CAS)**  complet, entièrement écrit en Python, ce qui la rend extrêmement  accessible et facile à intégrer dans l'écosystème Python, contrairement à  des logiciels propriétaires comme Mathematica ou Maple.[**[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQEDVmmR9Hfwr_bEg90hrhSGqJFIlUtdhYcSzxigaefC86iWuZJtHUzsp1LIichGRFPjoXydsPI4bMxXpsnVSmFwXy0T86sCYZRn2FtnGXq1Er3XzqzQBpfuyCWu3wid54c319NpSOI%3D)][[2](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQGDAMwhLJIsqi6RxCUIQyA1Kip5n6iH9QNhd6yByBHNFnZi84Zu03niO2fhApFLyL4tH54GLBtpx6iX2zcldTiBa6WJvXiDqQSD5ySAS3RyyAiCxJSuD0I-EECjz310aTLl3JjBRmfBdY70ty2T-EHNqSaP8DIvpPwSvoPA_BN2AiUOx1hs_GtWATiRu5KK)]

**Pour  un étudiant en Licence de Mathématiques, SymPy est un outil essentiel  car il permet de manipuler des expressions, des équations et des  fonctions **sous leur forme symbolique exacte**, sans approximations numériques.[**[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQEDVmmR9Hfwr_bEg90hrhSGqJFIlUtdhYcSzxigaefC86iWuZJtHUzsp1LIichGRFPjoXydsPI4bMxXpsnVSmFwXy0T86sCYZRn2FtnGXq1Er3XzqzQBpfuyCWu3wid54c319NpSOI%3D)][[3](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQGCjQELuaTNFp3wDiK_dnSSp_BBX1Vu2zaszPDgTU6ScCoqTipnOoQcrlD-Cg6peiFrk4sp4X2ZPhyj3TwsLtSnXqvKjKoCw1mNy5Z4rVXp9I8LefJ_DYzgBmmk6yYf1z9q2AyxeDFF9od2slNz6H6NKfV8q8ANC5j55UCuh9Dxe2r-gPVXKpiPZw_oIzzSXZXIgwcupcKqwm9S1cOUHw%3D%3D)]

---

## I. Concept Fondamental : La Différence entre Symbolique et Numérique

**La distinction fondamentale, cruciale pour un mathématicien, se fait entre SymPy et des bibliothèques comme NumPy :[**[2](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQGDAMwhLJIsqi6RxCUIQyA1Kip5n6iH9QNhd6yByBHNFnZi84Zu03niO2fhApFLyL4tH54GLBtpx6iX2zcldTiBa6WJvXiDqQSD5ySAS3RyyAiCxJSuD0I-EECjz310aTLl3JjBRmfBdY70ty2T-EHNqSaP8DIvpPwSvoPA_BN2AiUOx1hs_GtWATiRu5KK)]


| **Type de Calcul** | **Bibliothèque Exemple** | **Description** | **Résultat pour**`        2` |
| ------------------ | ------------------------- | --------------- | ----------------------------- |

```

    
```

Numérique**NumPy**Calcule des valeurs approchées (nombres à virgule flottante).**1.4142135623730951** (Valeur approchée)[[4](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQH7yhre5XCR0eV7xwJMA2IuGs1AdrOfm7ci-Oy3jefiDAeq3l3CPk08Hti_-p_siXo0XsjjQM5ebB1UsHO1b5_mLvyFuNE-DYlF6bgp3k2U7o49HUZ9foG8mtPXj2hXPTOGMtotmfCZKQ%3D%3D)]**Symbolique**SymPy**Manipule des symboles et conserve les expressions exactes.**

```
        2
```


| ``<br/>`      `(Expression exacte)[[4](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQH7yhre5XCR0eV7xwJMA2IuGs1AdrOfm7ci-Oy3jefiDAeq3l3CPk08Hti_-p_siXo0XsjjQM5ebB1UsHO1b5_mLvyFuNE-DYlF6bgp3k2U7o49HUZ9foG8mtPXj2hXPTOGMtotmfCZKQ%3D%3D)] |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

**C'est cette capacité à conserver l'**exactitude** (par exemple, manipuler **

```
        π
    
```

,

```
        e
    
```

,

```
        2
```

```

    
```

comme des symboles) qui rend SymPy indispensable en mathématiques.[[3](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQGCjQELuaTNFp3wDiK_dnSSp_BBX1Vu2zaszPDgTU6ScCoqTipnOoQcrlD-Cg6peiFrk4sp4X2ZPhyj3TwsLtSnXqvKjKoCw1mNy5Z4rVXp9I8LefJ_DYzgBmmk6yYf1z9q2AyxeDFF9od2slNz6H6NKfV8q8ANC5j55UCuh9Dxe2r-gPVXKpiPZw_oIzzSXZXIgwcupcKqwm9S1cOUHw%3D%3D)][[4](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQH7yhre5XCR0eV7xwJMA2IuGs1AdrOfm7ci-Oy3jefiDAeq3l3CPk08Hti_-p_siXo0XsjjQM5ebB1UsHO1b5_mLvyFuNE-DYlF6bgp3k2U7o49HUZ9foG8mtPXj2hXPTOGMtotmfCZKQ%3D%3D)][[5](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQFIAko0EHas6s45HOs8g6QmCkNHG9EZpkacraxZi5thK85k7ielCAGUBHq7rti3uUh96suhLVefYTOh6W_v-rydNYl3j64T8D5wSTPSN9dr6xOmfr0wqkAN2NGfJ7LXcU6Pgoq_9DI3M0k7cL87sgqvBBYKzSbXluoazFOYzbuCFunYTB6k6lszZA%3D%3D)]

---

## II. Les Bases de SymPy

### 1. Définir les Symboles

**Avant  d'effectuer tout calcul, il est impératif de déclarer les variables  comme des objets symboliques de SymPy à l'aide de la fonction **symbols()**.[**[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQEDVmmR9Hfwr_bEg90hrhSGqJFIlUtdhYcSzxigaefC86iWuZJtHUzsp1LIichGRFPjoXydsPI4bMxXpsnVSmFwXy0T86sCYZRn2FtnGXq1Er3XzqzQBpfuyCWu3wid54c319NpSOI%3D)][[2](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQGDAMwhLJIsqi6RxCUIQyA1Kip5n6iH9QNhd6yByBHNFnZi84Zu03niO2fhApFLyL4tH54GLBtpx6iX2zcldTiBa6WJvXiDqQSD5ySAS3RyyAiCxJSuD0I-EECjz310aTLl3JjBRmfBdY70ty2T-EHNqSaP8DIvpPwSvoPA_BN2AiUOx1hs_GtWATiRu5KK)]

**Exemple :**

** code **Python

```
    from sympy import symbols, sqrt, pi, E

# Déclaration de variables symboliques
x, y = symbols('x y')
a, b, c = symbols('a b c')

# Utilisation des constantes symboliques
expr_pi = 2 * pi 
expr_sqrt = 2 - sqrt(2)**2 # Résultat : 0 (exact)
  
```

### 2. Manipulation d'Expressions Algébriques

**SymPy  offre des fonctions pour manipuler des expressions, comme la  simplification, l'expansion ou la factorisation, ce qui est souvent  fastidieux à la main.[**[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQEDVmmR9Hfwr_bEg90hrhSGqJFIlUtdhYcSzxigaefC86iWuZJtHUzsp1LIichGRFPjoXydsPI4bMxXpsnVSmFwXy0T86sCYZRn2FtnGXq1Er3XzqzQBpfuyCWu3wid54c319NpSOI%3D)][[4](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQH7yhre5XCR0eV7xwJMA2IuGs1AdrOfm7ci-Oy3jefiDAeq3l3CPk08Hti_-p_siXo0XsjjQM5ebB1UsHO1b5_mLvyFuNE-DYlF6bgp3k2U7o49HUZ9foG8mtPXj2hXPTOGMtotmfCZKQ%3D%3D)]


| **Fonction**   | **Description**                                                            | **Exemple de Code**                     |
| -------------- | -------------------------------------------------------------------------- | --------------------------------------- |
| **expand()**   | **Développer une expression (ex:**`        (x+1)2→x2+2x+1`<br/>`      `) | **expand((x + 1)\*\*2)**                |
| **factor()**   | **Factoriser une expression**                                              | **factor(x\*\*2 + 2\*x + 1)**           |
| **simplify()** | **Simplifier une expression complexe (souvent trigonométrique)**          | **simplify(sin(x)\*\*2 + cos(x)\*\*2)** |

---

## III. Applications Clés en Analyse (Calcul Différentiel et Intégral)

**SymPy excelle dans les domaines de l'analyse, couvrant la dérivation, l'intégration, les limites et les séries.[**[3](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQGCjQELuaTNFp3wDiK_dnSSp_BBX1Vu2zaszPDgTU6ScCoqTipnOoQcrlD-Cg6peiFrk4sp4X2ZPhyj3TwsLtSnXqvKjKoCw1mNy5Z4rVXp9I8LefJ_DYzgBmmk6yYf1z9q2AyxeDFF9od2slNz6H6NKfV8q8ANC5j55UCuh9Dxe2r-gPVXKpiPZw_oIzzSXZXIgwcupcKqwm9S1cOUHw%3D%3D)][[5](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQFIAko0EHas6s45HOs8g6QmCkNHG9EZpkacraxZi5thK85k7ielCAGUBHq7rti3uUh96suhLVefYTOh6W_v-rydNYl3j64T8D5wSTPSN9dr6xOmfr0wqkAN2NGfJ7LXcU6Pgoq_9DI3M0k7cL87sgqvBBYKzSbXluoazFOYzbuCFunYTB6k6lszZA%3D%3D)][[6](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQHUsWqsNX6iBYwJgN8vW6jp3dW_ocwQsnKyPvQ5nZoQ0pIyNPaR3848vzZxxiMMO27q46c8K4VtggZYcZvxCF5Bx-rDKYzpXfV0evkDqm-uDK79Cr97eQS44_hn2HAwfKePPmyCvrjKIVSVakMPnJKZj5o-GuWyOm8%3D)]

### 1. Dérivation (diff)

**La fonction **diff(expression, variable)** calcule la dérivée de l'expression par rapport à la variable spécifiée.[**[4](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQH7yhre5XCR0eV7xwJMA2IuGs1AdrOfm7ci-Oy3jefiDAeq3l3CPk08Hti_-p_siXo0XsjjQM5ebB1UsHO1b5_mLvyFuNE-DYlF6bgp3k2U7o49HUZ9foG8mtPXj2hXPTOGMtotmfCZKQ%3D%3D)][[7](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQEUytuGiMWnDdtWv28KZcNRzl5a8rnNcPW0lo9zHuRlIK6BBvxaHkYwstay6XdgCmwxCXJ9q5GoXaoXTfrwoU77RYMVs2lAj-kWwxRabeCy_6KkRkFJcugWnu8pJFd05FsVRCrpO1iIBZesI8wOgool9SC0)]


| **Opération**          | **Fonction SymPy**   | **Exemple de Code**                                   | **Résultat**                                                                                                                                                                                                                                                                                   |
| ----------------------- | -------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Dérivée simple**    | **diff(expr, x)**    | **diff(x\*\*5, x)**                                   | **5\*x\*\*4**[[7](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQEUytuGiMWnDdtWv28KZcNRzl5a8rnNcPW0lo9zHuRlIK6BBvxaHkYwstay6XdgCmwxCXJ9q5GoXaoXTfrwoU77RYMVs2lAj-kWwxRabeCy_6KkRkFJcugWnu8pJFd05FsVRCrpO1iIBZesI8wOgool9SC0)] |
| **Dérivée partielle** | **diff(expr, x, y)** | **f = x\*\*2 \* y + 2\*x - log(y)**<br>**diff(f, x)** | **2\*x\*y + 2**[[4](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQH7yhre5XCR0eV7xwJMA2IuGs1AdrOfm7ci-Oy3jefiDAeq3l3CPk08Hti_-p_siXo0XsjjQM5ebB1UsHO1b5_mLvyFuNE-DYlF6bgp3k2U7o49HUZ9foG8mtPXj2hXPTOGMtotmfCZKQ%3D%3D)]       |
| **Ordre supérieur**    | **diff(expr, x, 2)** | **diff(sin(x), x, 2)**                                | **-sin(x)**                                                                                                                                                                                                                                                                                     |

### 2. Intégration (integrate)

**La fonction **integrate(expression, variable)** calcule l'intégrale indéfinie. Pour une intégrale définie, il faut ajouter un triplet **(variable, borne\_inf, borne\_sup)**.[**[6](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQHUsWqsNX6iBYwJgN8vW6jp3dW_ocwQsnKyPvQ5nZoQ0pIyNPaR3848vzZxxiMMO27q46c8K4VtggZYcZvxCF5Bx-rDKYzpXfV0evkDqm-uDK79Cr97eQS44_hn2HAwfKePPmyCvrjKIVSVakMPnJKZj5o-GuWyOm8%3D)][[8](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQFpdvefsoquE1BKsEGmGB40_9iCmVvqlYHfeYLMl-r-ZtYeKt_qDxTAg0C_27y5QEfQDBKMQXPhAk_R0HIWzK7P68XKx52v966E-shKmkzAiqPKB7tlm2harbI1sAPU1ESrO7_XYkXUybMOMJ5pd3hZIEusVPALfg5MaR-k_fFijiOTsRUWjMbqqQgkC2-oS-mPQFfcdx13xr7rl3Pq--Tudgi5VQUqT6VfqfI-qw%3D%3D)]

**Exemple de Code :**

** code **Python

```
    from sympy import integrate, sin, oo # 'oo' pour l'infini

# Intégrale indéfinie : ∫(sin(x)) dx
integrale_indefinie = integrate(sin(x), x)
# Résultat : -cos(x)

# Intégrale définie : ∫ de 0 à pi (sin(x)) dx
integrale_definie = integrate(sin(x), (x, 0, pi))
# Résultat : 2

# Intégrale impropre : ∫ de 0 à ∞ (e^(-x)) dx
from sympy import exp
integrale_impropre = integrate(exp(-x), (x, 0, oo))
# Résultat : 1
  
```

### 3. Limites (limit) et Séries (series)

** code **Python

```
    from sympy import limit, series

# Calcul de limite : lim_{x->0} (sin(x)/x)
limite = limit(sin(x)/x, x, 0)
# Résultat : 1

# Développement en série de Taylor autour de x=0
serie_taylor = sin(x).series(x, 0, 5) # Ordre 5
# Résultat : x - x**3/6 + O(x**5) (avec le terme d'erreur)
  
```

---

## IV. Résolution d'Équations (solve)

**La fonction **solve()**  est l'une des plus puissantes de SymPy, permettant de résoudre  symboliquement une ou plusieurs équations, linéaires ou non, pour  trouver les racines ou les solutions en fonction des autres variables.[**[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQEDVmmR9Hfwr_bEg90hrhSGqJFIlUtdhYcSzxigaefC86iWuZJtHUzsp1LIichGRFPjoXydsPI4bMxXpsnVSmFwXy0T86sCYZRn2FtnGXq1Er3XzqzQBpfuyCWu3wid54c319NpSOI%3D)][[3](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQGCjQELuaTNFp3wDiK_dnSSp_BBX1Vu2zaszPDgTU6ScCoqTipnOoQcrlD-Cg6peiFrk4sp4X2ZPhyj3TwsLtSnXqvKjKoCw1mNy5Z4rVXp9I8LefJ_DYzgBmmk6yYf1z9q2AyxeDFF9od2slNz6H6NKfV8q8ANC5j55UCuh9Dxe2r-gPVXKpiPZw_oIzzSXZXIgwcupcKqwm9S1cOUHw%3D%3D)][[9](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQHnfnyepKdcoHib8cmuE6E7H-IKgHcn-n9t6CH5u6jN7lIsAVxcnQJDl7PVWdCQixLFmVfIlVX2L8uT0ysiyz6ymBl-czACzncdQt9V9-NjaUpocb-Vajdwjm5n-WoezseMaF-Ui68vmxCI2KHCvUSXSMNlBy5h-SRk7g%3D%3D)]

**Exemple de Code (système d'équations) :**

** code **Python

```
    from sympy import solve, Eq

# Définition des variables symboliques
x, y = symbols('x y')

# Définition des équations :
# Équation 1 : x + y = 5  ->  x + y - 5 = 0
eq1 = Eq(x + y, 5) 
# Équation 2 : x^2 + y^2 = 17 -> x**2 + y**2 - 17 = 0
eq2 = Eq(x**2 + y**2, 17)

# Résolution du système : solve([eq1, eq2], (x, y))
solutions = solve([eq1, eq2], (x, y))
# Résultat : [(1, 4), (4, 1)] (deux paires de solutions (x, y))
  
```

---

## V. Algèbre Linéaire et Matrices

**Le module **Matrix** de SymPy permet de manipuler des matrices avec des éléments symboliques, ce qui est essentiel en algèbre linéaire.[**[7](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQEUytuGiMWnDdtWv28KZcNRzl5a8rnNcPW0lo9zHuRlIK6BBvxaHkYwstay6XdgCmwxCXJ9q5GoXaoXTfrwoU77RYMVs2lAj-kWwxRabeCy_6KkRkFJcugWnu8pJFd05FsVRCrpO1iIBZesI8wOgool9SC0)][[8](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQFpdvefsoquE1BKsEGmGB40_9iCmVvqlYHfeYLMl-r-ZtYeKt_qDxTAg0C_27y5QEfQDBKMQXPhAk_R0HIWzK7P68XKx52v966E-shKmkzAiqPKB7tlm2harbI1sAPU1ESrO7_XYkXUybMOMJ5pd3hZIEusVPALfg5MaR-k_fFijiOTsRUWjMbqqQgkC2-oS-mPQFfcdx13xr7rl3Pq--Tudgi5VQUqT6VfqfI-qw%3D%3D)][[10](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQGd_pcV6ysNi_tYW8lDFbw94efnQgYTweCNy6g_g0nPKKT3P36XdcmQKEOwnx0_0cz_gkIUZvFWMIb7MpYPEGEtI8tgbaSHZ1RLxzqwi16Ad0cvOL6_KelPKyD-pUgM2s2eKFUO9fviZ4iI6r5wObBF9pyeauFqtLWuWSrVsqGA)][[11](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQHe9we-Fq2nc5PdFglHsm4F8yWzV8mrsGSrcfHVPmnbSlrvOslbol1JGrhJFT8eKXfC28SC-B16GGInM3KK7JQOI4HJ9ak_dEkLIL1Yy2AG9fJchYoZJsBOaha1tqdKH6CuiOvAA0jy3acTqJliC--Ipk0oJnziOA%3D%3D)]

**Exemple de Code :**

** code **Python

```
    from sympy import Matrix, symbols

# Définition des variables pour la matrice symbolique
x, y = symbols('x y')

# Création de deux matrices
M = Matrix([[x, 1], [0, y]])
N = Matrix([[1, 2], [3, 4]])

# Opérations de base
produit = M * N         # Multiplication matricielle (M.dot(N) est aussi possible)
determinant = M.det()   # Calcul du déterminant
inverse = M**-1         # Calcul de l'inverse

# Calcul de l'Échelon Réduit par les lignes (Reduced Row Echelon Form - RREF)
# Utile pour résoudre des systèmes linéaires ou trouver le rang
M_rref, pivots = N.rref() 
# M_rref donne la matrice échelonnée réduite, pivots donne les indices des colonnes pivots
  
```

Sources ** help **

1. [youtube.com](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQEDVmmR9Hfwr_bEg90hrhSGqJFIlUtdhYcSzxigaefC86iWuZJtHUzsp1LIichGRFPjoXydsPI4bMxXpsnVSmFwXy0T86sCYZRn2FtnGXq1Er3XzqzQBpfuyCWu3wid54c319NpSOI%3D)
2. [geeksforgeeks.org](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQGDAMwhLJIsqi6RxCUIQyA1Kip5n6iH9QNhd6yByBHNFnZi84Zu03niO2fhApFLyL4tH54GLBtpx6iX2zcldTiBa6WJvXiDqQSD5ySAS3RyyAiCxJSuD0I-EECjz310aTLl3JjBRmfBdY70ty2T-EHNqSaP8DIvpPwSvoPA_BN2AiUOx1hs_GtWATiRu5KK)
3. [readthedocs.io](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQGCjQELuaTNFp3wDiK_dnSSp_BBX1Vu2zaszPDgTU6ScCoqTipnOoQcrlD-Cg6peiFrk4sp4X2ZPhyj3TwsLtSnXqvKjKoCw1mNy5Z4rVXp9I8LefJ_DYzgBmmk6yYf1z9q2AyxeDFF9od2slNz6H6NKfV8q8ANC5j55UCuh9Dxe2r-gPVXKpiPZw_oIzzSXZXIgwcupcKqwm9S1cOUHw%3D%3D)
4. [github.io](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQH7yhre5XCR0eV7xwJMA2IuGs1AdrOfm7ci-Oy3jefiDAeq3l3CPk08Hti_-p_siXo0XsjjQM5ebB1UsHO1b5_mLvyFuNE-DYlF6bgp3k2U7o49HUZ9foG8mtPXj2hXPTOGMtotmfCZKQ%3D%3D)
5. [problemsolvingwithpython.com](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQFIAko0EHas6s45HOs8g6QmCkNHG9EZpkacraxZi5thK85k7ielCAGUBHq7rti3uUh96suhLVefYTOh6W_v-rydNYl3j64T8D5wSTPSN9dr6xOmfr0wqkAN2NGfJ7LXcU6Pgoq_9DI3M0k7cL87sgqvBBYKzSbXluoazFOYzbuCFunYTB6k6lszZA%3D%3D)
6. [slabbe.org](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQHUsWqsNX6iBYwJgN8vW6jp3dW_ocwQsnKyPvQ5nZoQ0pIyNPaR3848vzZxxiMMO27q46c8K4VtggZYcZvxCF5Bx-rDKYzpXfV0evkDqm-uDK79Cr97eQS44_hn2HAwfKePPmyCvrjKIVSVakMPnJKZj5o-GuWyOm8%3D)
7. [tresfacile.net](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQEUytuGiMWnDdtWv28KZcNRzl5a8rnNcPW0lo9zHuRlIK6BBvxaHkYwstay6XdgCmwxCXJ9q5GoXaoXTfrwoU77RYMVs2lAj-kWwxRabeCy_6KkRkFJcugWnu8pJFd05FsVRCrpO1iIBZesI8wOgool9SC0)
8. [osaka-u.ac.jp](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQFpdvefsoquE1BKsEGmGB40_9iCmVvqlYHfeYLMl-r-ZtYeKt_qDxTAg0C_27y5QEfQDBKMQXPhAk_R0HIWzK7P68XKx52v966E-shKmkzAiqPKB7tlm2harbI1sAPU1ESrO7_XYkXUybMOMJ5pd3hZIEusVPALfg5MaR-k_fFijiOTsRUWjMbqqQgkC2-oS-mPQFfcdx13xr7rl3Pq--Tudgi5VQUqT6VfqfI-qw%3D%3D)
9. [geeksforgeeks.org](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQHnfnyepKdcoHib8cmuE6E7H-IKgHcn-n9t6CH5u6jN7lIsAVxcnQJDl7PVWdCQixLFmVfIlVX2L8uT0ysiyz6ymBl-czACzncdQt9V9-NjaUpocb-Vajdwjm5n-WoezseMaF-Ui68vmxCI2KHCvUSXSMNlBy5h-SRk7g%3D%3D)
10. [purdue.edu](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQGd_pcV6ysNi_tYW8lDFbw94efnQgYTweCNy6g_g0nPKKT3P36XdcmQKEOwnx0_0cz_gkIUZvFWMIb7MpYPEGEtI8tgbaSHZ1RLxzqwi16Ad0cvOL6_KelPKyD-pUgM2s2eKFUO9fviZ4iI6r5wObBF9pyeauFqtLWuWSrVsqGA)
11. [sympy.org](https://www.google.com/url?sa=E&q=https%3A%2F%2Fvertexaisearch.cloud.google.com%2Fgrounding-api-redirect%2FAUZIYQHe9we-Fq2nc5PdFglHsm4F8yWzV8mrsGSrcfHVPmnbSlrvOslbol1JGrhJFT8eKXfC28SC-B16GGInM3KK7JQOI4HJ9ak_dEkLIL1Yy2AG9fJchYoZJsBOaha1tqdKH6CuiOvAA0jy3acTqJliC--Ipk0oJnziOA%3D%3D)

##### Google Search Suggestions

Display of Search Suggestions is required when using Grounding with Google Search. [ Learn more ](https://ai.google.dev/gemini-api/docs/grounding/search-suggestions)

![Google logo](https://www.gstatic.com/images/branding/productlogos/googleg/v6/24px.svg)

** 20,1s **

Use Arrow Up and Arrow Down to select a turn, Enter to jump to it, and Escape to return to the chat.

[ ]

Response ready.
