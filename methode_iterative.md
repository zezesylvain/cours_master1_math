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
