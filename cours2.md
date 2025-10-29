# Interpolation Polynomiale

## Methode de Lagrange

Soit $f(x)$ une fonction definie de $ [a, b] \rightarrow \mathbb{R}$

soit une subdivision $X_n$ de $[a, b]$, $a=x_0<x_1<x_2<\ldots<x_n=b$

L'interpolation de Lagrange consiste a trouver un polynome $P(x)$ tel que:

$P(x_i) = f(x_i)\; \forall i \in [0, n] $

$$
P(x) = \sum_{i=0}^n L_i(x)f(x_i)\\
avec \\
L_i(x) = \prod_{j= 0,\ j\neq i}^n \frac{x-x_j}{x_i-x_j}
$$

### Algorithme

$f(x)$ une fonction definie de $ [a, b] \rightarrow \mathbb{R}$

$X_n \Rightarrow a=x_0<x_1<x_2<\ldots<x_n=b$ une subdivision de 'intervalle $[a, b]$

1. Calcul de $L_i(x)$
2. Calcul de $P(x)$
3. Calcul de l'erreur $E(x) = log(|f(x)-P(x)|+\epsilon)$ avec $\epsilon = 10^{-15}$
4. Representation graphique
   1. $f(x)$ et $P(x)$ sur le meme graphique
   2. $E(x)$ sur un autre graphique

### Code

1. Dependances:
   1. numpy
   2. matplotlib.pyplot
2. Fichier des dependances:
   1. pip freeze > requirements.txt
3. Installation des dependances:
   1. pip install numpy
   2. pip install matplotlib
4. Mise a jour du fichier des dependances
   1. pip freeze > requirements.txtpip
5. Pour ceux qui auront le projet
   1. pip install -r requirements.txt

#### Calcul de log de :

1. 245
2. 19802
3. 2
4. 0.1
5. 0.0008
6. 0.23
7. 2.445

## Methode Spline quadratique

Soit $f(x)$ une fonction definie de $ [a, b] \rightarrow \mathbb{R}$

soit une subdivision $X_n$ de $[a, b]$, $a=x_0<x_1<x_2<\ldots<x_n=b

L'interpolation par la methode de Spline quadratique consiste a trouver un polynome $S(x)$

defini par morceau repondant aux criteres suivants:

$$
H_1 \rightarrow S(x) \text{ est de degre 2 sur chauqe morceau}\\
H_2 \rightarrow S(x_i) = f(x_i) \Rightarrow \text{Critere de interpolation}\\
H_3 \rightarrow S \text{ est continue}\\
H_4 \rightarrow  S' \text{ est continue}
$$

$$
S(x) = 
\begin{cases}
S_0(x) \; si \; x\in[x_0, x_1]\\
S_1(x) \; si \; x\in[x_1, x_2]\\
\ldots\\
S_{i}(x) \; si \; x = [x_i, x_{i+1}]\\
\ldots\\
S_{n-1}(x) \; si \; x\in[x_{n-1}, x_n]

\end{cases}
$$

### Mise en equations

$H_1$

$$
S(x) = 
\begin{cases}
S_0(x) = a_0(x-x_0)^2+b_0(x-x_0)+c_0 \; si \; x\in[x_0, x_1]\\
S_1(x) = a_1(x-x_1)^2+b_1(x-x_1)+c_1 \; si \; x\in[x_1, x_2]\\
\ldots\\
S_{i}(x)= a_i(x-x_i)^2+b_i(x-x_i)+c_i \; si \; x = [x_i, x_{i+1}]\\
\ldots\\
S_{n-1}(x)= a_{n-1}(x-x_{n-1})^2+b_{n-1}(x-x_{n-1})+c_{n-1} \; si \; x\in[x_{n-1}, x_n]

\end{cases}
$$

Cela nous donne $n$ polynome de second degre soit 3 coefficients inconnues par equation.

Nous avons donc $3n$ inconnues

$ H_2  \rightarrow S(x_i) = f(x_i) \;\forall i = 0, 1, \cdots, n \text{ soit n+1 equations}$

$H_3 \rightarrow S \text{ est continue}$

$$
S_i(x_{i+1})=S_{i+1}(x_{i+1}) \;\forall i = 0, 1, \dots, n-2 \; soit\; n-1 \; equations
$$

$H_4 \rightarrow S' \text{ est continue}$

$S'_i(x_{i+1})=S'_{i+1}(x_{i+1}) \;\forall i = 0, 1, \dots, n-2 \; soit\; n-1 \; equations$

$$
H_2  : S(x_i) = f(x_i)\\
\Rightarrow S_i(x_i) = f(x_i)\\
\Rightarrow S_i(x_i) = c_i = f(x_i)=y_i \; \forall i=0,1,\dots,n-1\\
$$

$H_4$

$$
S'_i(x) = 2a_i(x-x_i)+b_i\\
Posons \\
z_i = S'(x_i) \; \forall i=0,1,\dots,n\\
S'(x_i) = S'_i(x_i)= b_i \; \forall i =0,1,\dots,n-1\\
b_i = z_i \; \forall i =0,1,\dots,n-1
$$

$$
S'_i(x) = 2a_i(x-x_i)+z_i\\
S_i(x) = a_i(x-x_i)^2+z_i(x-x_i)+y_i
$$

$$
H_4: \; continuite \; de\; S'(x)\; \\
S'_i(x_{i+1})=S'_{i+1}(x_{i+1})\\
2a_i(x_{i+1}-x_i)+z_i = z_{i+1}\\
a_i = \frac{z_{i+1}-z_i}{2(x_{i+1}-x_i)} \;\; (eq20)
$$

$$
H_3: Continuite \; de \; S(x)\\
S_i(x_{i+1})=S_{i+1}(x_{i+1})\\
a_i(x_{i+1}-x_i)^2+z_i(x_{i+1}-x_i)+y_i= y_{i+1} \;\; (eq30)
$$

En injectant la valeur de $a_i$ de $eq20$ dans $eq30$, on obtient:

$$
\frac{z_{i+1}-z_i}{2(x_{i+1}-x_i)}(x_{i+1}-x_i)^2+z_i(x_{i+1}-x_i)+y_i= y_{i+1}\\
\frac{1}{2}(z_{i+1}-z_i)(x_{i+1}-x_i)+z_i(x_{i+1}-x_i)+y_i= y_{i+1}\\
(x_{i+1}-x_i)(\frac{1}{2}(z_{i+1}-z_i)+z_i)= y_{i+1}-y_i\\
(x_{i+1}-x_i)(\frac{1}{2}z_{i+1}-\frac{1}{2}z_i+z_i)= y_{i+1}-y_i\\
(x_{i+1}-x_i)(\frac{1}{2}z_{i+1}+\frac{1}{2}z_i)= y_{i+1}-y_i\\
\frac{1}{2}(x_{i+1}-x_i)(z_{i+1}+z_i)= y_{i+1}-y_i\\
z_{i+1}+z_i = \frac{2(y_{i+1}-y_i)}{x_{i+1}-x_i}\\
z_{i+1}= \frac{2(y_{i+1}-y_i)}{x_{i+1}-x_i}-z_i
$$

En fixant $S'(x_0)=f'(x_0)=z_0$, on determine tous les $z_i$

0___1_____2___............___i_________i+1________...........___n

$$
z_o = f'(x_0) \; ou \; z_0 = 0\\
z_{i+1} = \frac{2(y_{i+1}-y_i)}{x_{i+1}-x_i}-z_i \; \forall i = 0,1,\dots,n\\
S_i(x) = \frac{z_{i+1}-z_i}{2(x_{i+1}-x_i)}(x-x_i)^2-z_i(x-x_i)+y_i \; \forall i = 0,1,\dots,n-1
$$

## Probleme

$f(x): [a, b] \rightarrow \mathbb{R}$

$X_n$ une subdivision: $a = x_0<x_1<x_2<\dots,x_i<\dots<x_n=b$

$$
S(x) = 
\begin{cases}
S_0(x) = a_0(x-x_0)^2+b_0(x-x_0)+c_0 \; si \; x\in[x_0, x_1[\\
S_1(x) = a_1(x-x_1)^2+b_1(x-x_1)+c_1 \; si \; x\in[x_1, x_2[\\
\ldots\\
S_{i}(x)= a_i(x-x_i)^2+b_i(x-x_i)+c_i \; si \; x = [x_i, x_{i+1}[\\
\ldots\\
S_{n-1}(x)= a_{n-1}(x-x_{n-1})^2+b_{n-1}(x-x_{n-1})+c_{n-1} \; si \; x\in[x_{n-1}, x_n]

\end{cases}
$$

$S(x_n) = S_{n-1}(x_n)$

$$
z_o = f'(x_0) \; ou \; z_0 = 0\\
z_{i+1} = \frac{2(y_{i+1}-y_i)}{x_{i+1}-x_i}-z_i \; \forall i = 0,1,\dots,n\\
S_i(x) = \frac{z_{i+1}-z_i}{2(x_{i+1}-x_i)}(x-x_i)^2-z_i(x-x_i)+y_i \; \forall i = 0,1,\dots,n-1
$$

# Algo Spline Quadratique

1. Calcul des $y_i$
2. Definition des variables:
   1. $points$ L'ensemble des points pour evaluer $S$ et $f$
   2. $sol_{approchee}$ Resultats de $S(x)$
   3. $sol_{exacte}$ Evaluation de $f(x)$
   4. Calcul de $z_0 = f'(x_0)$
   5. $nb $: le nombre de points pour evaluer $S$ sur chaque intervalle $[x_i, x_{i+1}[$
3. Pour $i$ allant de 0 a $n-1$ faire
   1. Calcul de $z_{i+1} \forall i=1,\dots n-1$
   2. Calcul de $S_i(x)$
   3. Subdivision $X_i$ de l'intervalle $[x_i, x_{i+1}]$ en $nb+1$ points
      1. On ajoute la subdivision $X_i$ dans $Points$ sauf le dernier point de $X_i$, c'est-a-dire tous les elements de $X_i$ sauf $x_{i+1}$
   4. Evaluation de $S_i$ aux points $X_i$ sauf au dernier point $x_{i+1}$ pour avoir $Y_{eval}^i$
      1. On ajoute $Y_{eval}^i$ dans $sol_{approchee}$
4. on ajoute $x_n$ dans $points$
5. On calcule $S(x_n)=S_{n-1}(x_n)$ et on l'ajoute dans $sol_{approchee}$
6. On evalue $f$ en tous les elements de $points$ pour obtenir $sol_{exacte}$
7. On calcule l'erreur $Erreur = log(|sol_{exacte} - sol_{approchee}| + \epsilon)$ avec $\epsilon = 10^{-15}$
8. On trace les graphique
   1. $sol_{exacte}$ et $sol_{approchee}$ sur le meme graphique
   2. Erreur sur un autre graphique




# Git: C'est quoi?
