#Remplir le tableau
n = int(input("Donner le nombre des éléments : "))
T =[]
for i in range(n):
    v = float(input(f"Donner T[{i}] : "))
    T.append(v)

Max = max(T)
Min = min(T)
pmax = T.index(Max)
pmin = T.index(Min)
print(f"Le max est {Max} dans la position {pmax}")
print(f"Le max est {Min} dans la position {pmin}")