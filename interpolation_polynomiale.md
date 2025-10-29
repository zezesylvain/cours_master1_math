# Interpolation Polynomiale

Soit $f$ une fonction definie 👍

$$
f: [a, b] \rightarrow \mathbb{R}\\
x: \rightarrow f(x)
$$

Soit une subdivision $X_n$ telle que:

$$
X_n: a =x_0<x_1<x_2<\dots<x_n = b
$$

L'interpolation de Lagrance de la founction $f$  sur l'intervalle $[a, b]$  consiste a trouver un polynome $P$ tel que:

$$
P(x_i) = f(x_i) \;\forall i = 0, 1, \dots, n
$$

## Interpolation de Lagrange

Le polynome d'interpolation de Lagrange $P$ de la fonction $f$ est definie par:

$$
P(x) = \sum_{i=1}^n f(x_i)L_i(x)
$$

avec

$$
L_i(x) = \prod_{j=1, j\neq i}^n \frac{x-x_j}{x_i-x_j}
$$

## Interploation par spline quadratique

Interpoler $f$ par une spline quadratique consiste a trouver un polynome $S$ defini par morceau, continu et a derivee continue et de degreé 2 sur chaque morceau.

Considerons la subdivision $X_n$, $X_n: a =x_0<x_1<x_2<\dots<x_n = b$

on a : $S(x_i) = f(x_i)  \; \forall x_i \in X_n$

$S$ est continue et $S'$ est  continue

$$
S(x) = 
\begin{cases}
S_0(x) \; si \; x\in [x_0, x_1]\\
S_1(x) \; si \; x\in [x_1, x_2]\\
S_2(x) \; si \; x\in [x_2, x_3]\\
\cdots\\
S_i(x) \; si \; x\in [x_i, x_{i+1}]\\
\cdots\\
S_{n-1}(x) \; si \; x\in [x_{n-1}, x_n]\\
\end{cases}
$$

Chaque $S_i$ est un polynome de degreé 2 c'est-a-dire que:

$$
S(x) = 
\begin{cases}
S_0(x) = a_0x^2+b_0x+c_0 \; si \; x\in [x_0, x_1]\\
S_1(x) = a_1x^2+b_1x+c_1 \; si \; x\in [x_1, x_2]\\
S_2(x) = a_2x^2+b_2x+c_2\; si \; x\in [x_2, x_3]\\
\cdots\\
S_i(x) = a_ix^2+b_ix+c_i\; si \; x\in [x_i, x_{i+1}]\\
\cdots\\
S_{n-1}(x) = a_{n-1}x^2+b_{n-1}x+c_{n-1}\; si \; x\in [x_{n-1}, x_n]\\
\end{cases}
$$

Chaque $S_i(x) = a_ix^2+b_ix+c_i$ represente 3 inconnues, or nous avons $i=0, 1, \dots, n-1$ soit $n$ fonctions $S_i$  Ce qui nous donne $3n$ inconnues

# Hypotheses

## Hypothese 1: Interpolation $S(x_i) = f(x_i)$ $\forall i=0, 1, \dots, n$ soit $(n+1)$ Equations

## Hypothese 2: $S$ continue: $S_ {i-1}(x_i)=S_i(x_i)$ $\forall i=1, 2, \dots, n-1$ soit $(n-1)$ Equations

## Hypothese 2: $S'$ continue: $S'_ {i-1}(x_i)=S'_i(x_i)$ $\forall i=1, 2, \dots, n-1$ soit $(n-1)$ Equations

## $(n+1) + (n-1) +(n-1) = 3n-1$ Equations pour $3n$ inconnues

## Ce qui signifie que nous avons une solution a une constante pres

# Resolution

## Posons $  S_i(x) = a_i(x-x_i)^2+b_i(x-x_i) + c_i \;\; (eq3)$

ce qui donne:

## Hypothse 1: $c_i = f(x_i) \;\; (eq5)$

## Derivee S_i)$  : $ : $S'_i(x)= 2a_i(x-x_i)+b_i$

## Posons $ S'(x_i) = z_i = S'_i(x_i)$

Ce qui nous donne

## $b_i = z_i$ $\forall i = 1 \; , 2, \dots,  n-1 \;\; (eq10) $

## Continuiteé de $S'$

$$
S'_{i-1}(x_i) = S'_i(x_i) = z_i\\
2a_{i-1}(x_i-x_{i-1})+b_{i-1} = z_i\\
2a_{i-1}(x_i-x_{i-1}) = z_i - z_{i-1}\\
a_{i-1} = \frac{1}{2} \frac{z_i - z_{i-1}}{x_i-x_{i-1}} \;\; (eq20)
$$

## Continuite de $S$ soit $S_ {i-1}(x_i)=S_i(x_i)$

$$
🎉️ \;\; (eq30)
$$

Les coefficients $z_i$ sont determines si le terme de depart $z_0$ est connu.

## Reecrivons $(eq3)$ avec les nouvelles valeurs des coefficients:

$$
S_i(x) = S_i(x) = a_i(x-x_i)^2+b_i(x-x_i) + c_i\\
S_i(x) = \frac{1}{2} \frac{z_{i+1} - z_i}{x_{i+1}-x_i}(x-x_i)^2+z_i(x-x_i)^2+f(x_i) \;\; (eq40)
$$

## $z_0 = S'(x_0)$

si la fonction $f$ est connue, on prend:

## $z_0 = S'(x_0) = f'(x_0)$

sinon on prend

## $z0=S′(x0)=0z_0 = S'(x_0) = 0$


## Algo

### 1- $f(x)$, $a, b$, $X_n = \{a=x_0<x_1<x_2<\dots<x_n=b\}$

### 1-1- Calcul des $y_i = f(x_i)$


### 2- $z_0=f'(x_0)$

### 3- Calcul de $zi$:  $z_i = 2 \frac {y_i - y_{i-1}} {x_i-x_{i-1}} - z_ {i-1}$ $\forall i=1, 2, \dots n$

## 4- $S_i(x) = \frac{1}{2} \frac{z_{i+1} - z_i}{x_{i+1}-x_i}(x-x_i)^2+z_i(x-x_i)^2+f(x_i)$




# Librairie Sympy, Numpy
