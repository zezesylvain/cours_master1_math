# Interpolation Polynomiale

## Methode de Lagrange

Soit $f(x)$ une fonction definie de $ [a, b] \rightarrow \mathbb{R}$

soit une subdivision $X_n$ de $[a, b]$, $a=x_0<x_1<x_2<\ldots<x_n=b$

Linterpolation de Lagrange consiste a trouver un polynome $P(x)$ tel que:

$P(x_i) = f(x_i)\; \forall i \in [0, n] $

$$
P(x) = \sum_{i=0}^n L_i(x)f(x_i)\\
avec \\
L_i(x) = \prod_{j= 0,\ j\neq i}^n \frac{x-x_j}{x_i-x_j}
$$

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

En fixant $'(x_0)=0=z_0$, on determine tous les $z_i$

0___1_____2___............___i_________i+1________...........___n


$$
z_o = 0\\
z_{i+1} = \frac{2(y_{i+1}-y_i)}{x_{i+1}-x_i}-z_i \; \forall i = 0,1,\dots,n\\
S_i(x) = \frac{z_{i+1}-z_i}{2(x_{i+1}-x_i)}(x-x_i)^2-z_i(x-x_i)+y_i \; \forall i = 0,1,\dots,n-1
$$
