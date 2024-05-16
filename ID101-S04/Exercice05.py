n = int(input("Donner le nombre des éléments : "))
T =[]
for i in range(n):
    x = int(input(f"Donner l'élément {i+1} : "))
    T.append(x)
S = 0
P = 1
for e in T:
    S +=e
    P *=e
M = S/len(T)
print(f"S :{S}; P:{P}; M :{M}")
S = sum(T)
from functools import reduce
P = reduce(lambda a,b : a*b,T,1)
M = S/len(T)
print(f"S :{S}; P:{P}; M :{M}")