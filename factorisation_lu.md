# Factorisation LU

## Resolution de $Ax=b$ par la factorisation $LU$

$$
Ax=b\\
A = LU\\
LUx=b\\
y = Ux\\
Ly=b
$$

$$
[L, U, P] = lu(A)\\
PA=LU\\
Ax=b\\
PAx=Pb\\
LUx = Pb\\
Ux=y \rightarrow \text{ Systeme lineaire triangulaire superieur}\\
Ly=Pb \rightarrow \text{ systeme lineaire triangulaire inferieur}\\
$$

```python
# Un Algorythme est un ensemble d'etapes ordonnees qui permettent de resoudre un probleme
# Ax = b
"""
Donnees ; A, b
On va decomposer A en LU
[L, U, P] = lu(A) 
Resolution du systeme triangulaire inferieur Ly = Pb
Resolution du systeme triangulaire superieur Ux = y

"""
def Resolution_systeme_lneaire_par_lu(A,b):
   L, U, P = lu(A)

   
```
