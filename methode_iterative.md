# Methodes iteratives $Ax=b$


## Cas General $A = M-N$

$$
Ax=b\\
A = M-N\\


$$

On suppose qu'il existe une suite $x^k$

$$
\begin{cases}
x^0\\
x^{k+1} = M^{-1}Nx^k + d
\end{cases}
\\
\text{avec } d = M^{-1}b


$$

## Algo

$$
\text{Donnees: } A, b, x^0, \epsilon, NB_{iterMax}\\
[M, N] = CalculeMN(A)\\
x\leftarrow x^0\\
nb_{iter} = 0\\
\text{Tant que } ||Ax-b||>\epsilon \text{ et } nb_{iter} < NB_{iterMax}\\
\;\;\;\; x_{new} = M^{-1}Nx + d\\
\;\;\; \; x\leftarrow x_{new}\\
\;\;\;\;nb_{iter} = nb_{iter}+1\\
\text{Fin Tant que\;\;\;\;\;\;.\;\     .\;\; \quad ..\;\; \quad ..\;\; \quad ..\;\; \quad ..\;\; \quad .}\\
\text{Si } nb_{iter} < NB_{iterMax} \; Alors\\
\; \text{Solution est } x\\
sinon \;\\\text{\;\;\; Pas de solution}
$$


# Determination du schema

$$
Mx^{k+1} = Nx^k + b
$$


$$
A = M-N\\
A = D+E+F
$$

## Jacobi: $M = D$ et $N=-E-F$

$$
Mx^{k+1} = Nx^k + b \Rightarrow (Mx^{k+1})_i = (Nx^k+b)_i \;\;\; (eq_1)\\
(Mx^{k+1})_i = \sum_{j=1}^nM_{i,j}x^{k+1}_j \;\;\; (eq_2)\\
(Nx^k+b)_i = \sum_{j=1}^nN_{i,j}x^k_j + b_i \;\;\; (eq_3)
$$

$$
M = D \Rightarrow M_{i,j} = D_{i,j} = 
\begin{cases}
0 \; si \; i \neq j\\
a_{i,i} \; si \; i= j

\end{cases}
\;\;\; (eq_4)
$$

$$
N = -E-F\Rightarrow N_{i,j} = -E_{i,j}-F_{i,j} = 
\begin{cases}
0 \; si \; i = j\\
-a_{i,j} \; si \; i\neq j

\end{cases}
\;\;\; (eq_5)
$$



En injectant $(eq4)$ dans $(eq2)$, on obtient:

$$
(Mx^{k+1})_i = \sum_{j=1}^nM_{i,j}x^{k+1}_j = \sum_{j=1}^{i-1}M_{i,j}x^{k+1}_j + M_{i,i}x^{k+1}_i+\sum_{j=i+1}^n M_{i,j}x^{k+1}_j\\
(Mx^{k+1})_i = a_{i,i}x^{k+1}_i \;\;\; (eq6)
$$


En injectant $(eq5)$ dans $(eq3)$, on obtient:

$$
(Nx^k+b)_i = \sum_{j=1}^nN_{i,j}x^k_j + b_i = \sum_{j=1}^{i-1}N_{i,j}x^k_j + N_{i,i}x^k_i +\sum_{j=i+1}^n N_{i,j}x^k_j + b_i\\
(Nx^k+b)_i = -\sum_{j=1}^{i-1}a_{i,j}x^k_j - \sum_{j=i+1}^n a_{i,j}x^k_j + b_i\\
(Nx^k+b)_i = -\sum_{j=1, j\neq i}^{n}a_{i,j}x^k_j+ b_i \; \; \; (eq7)
$$

L'equation $(eq1)$ devient:

$$
a_{i,i}x^{k+1}_i = -\sum_{j=1, j\neq i}^{n}a_{i,j}x^k_j+ b_i\\
\Rightarrow 

x^{k+1}_i = \frac{b_i - \sum_{j=1, j\neq i}^{n}a_{i,j}x^k_j}{a_{i,i}} \;\;\; (eq10)
$$



## Gauss Seidel: $M=D+E$ et $N=-F$


Nous avon donc:

$$
M = D+E \Rightarrow M_{i,j} = D_{i,j}+E_{i,j}= 
\begin{cases}
0 \; si \; i < j\\
a_{i,j} \; si \; i\geq j

\end{cases}
\;\;\; (eq20)
$$

et

$$
N = -F\Rightarrow N_{i,j} = -F_{i,j} = 
\begin{cases}
0 \; si \; i \geq j\\
-a_{i,j} \; si \; i < j

\end{cases}
\;\;\; (eq21)
$$

La quantiteé $(Mx^{k+1})_i$ devient

$$
(Mx^{k+1})_i = \sum_{j=1}^n M_{i,j}x^{k+1}_j = \sum_{j=1}^{i-1} M_{i,j}x^{k+1}_j + M_{i,i}x^{k+1}_i + \sum_{j=i+1}^n M_{i,j}x^{k+1}_j\\
(Mx^{k+1})_i = \sum_{j=1}^{i-1} a_{i,j}x^{k+1}_j + a_{i,i}x^{k+1}_i \;\;\; (eq22)
$$

Et pour la quantiteé $(Nx^k+b)_i$, nous avons:

$$
(Nx^k+b)_i = \sum_{j=1}^nN_{i,j}x^k_j + b_i = \sum_{j=1}^{i-1}N_{i,j}x^k_j + N_{i,i}x^k_i +\sum_{j=i+1}^n N_{i,j}x^k_j + b_i\\
(Nx^k+b)_i = -\sum_{j=i+1}^n N_{i,j}x^k_j + b_i\\
(Nx^k+b)_i = b_i -\sum_{j=i+1}^n a_{i,j}x^k_j \;\;\; (eq23)
$$



En faisant $(eq22) = (eq23)$, nous obtenons:

$$
\sum_{j=1}^{i-1} a_{i,j}x^{k+1}_j + a_{i,i}x^{k+1}_i = b_i -\sum_{j=i+1}^n a_{i,j}x^k_j\\
a_{i,i}x^{k+1}_i = b_i -\sum_{j=i+1}^n a_{i,j}x^k_j - \sum_{j=1}^{i-1} a_{i,j}x^{k+1}_j\\
x^{k+1}_i = \frac{b_i -\sum_{j=i+1}^n a_{i,j}x^k_j - \sum_{j=1}^{i-1} a_{i,j}x^{k+1}_j}{a_{i,i}}
$$



## Relaxation: $M=\frac {1} {\omega}(D-\omega E)$ et $N=(1-\omega)D-F$


$$
(Ax)_i = \sum_{j=1}^n a_{i,j}x_j
$$
