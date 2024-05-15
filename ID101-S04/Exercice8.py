T =[10,14,50,5,20,150,80,44,77,4]
Min = T[0]
Max = T[0]
pmin = 0
pmax = 0

# pour i de  0 à N - 1 Faire
# Si T[i] < min Alors
#     min = T[i]
#     pmin = i
# FinSi

# Si T[i] > max Alors
#     max = T[i]
#     pmax = i
# FinSi
# finpour
for i in range(len(T)):
    if T[i] < Min :
        Min = T[i]
        pmin = i
    if T[i]> Max:
        Max = T[i]
        pmax = i
# Ecrireln("Le max est ",max, " dans la position ",pmax)
# Ecrireln("Le min est ",min, " dans la position ",pmin)
print(f"le max est {Max} dans la position {pmax}")
print(f"le max est {Min} dans la position {pmin}")

Max = max(T)
Min = min(T)
pmin = T.index(Min)
pmax = T.index(Max)
print(f"le max est {Max} dans la position {pmax}")
print(f"le max est {Min} dans la position {pmin}")


L=sorted(T)
min=L[0]
max=L[-1]
print(T)
print(f"{min} est le minimum dans la position {T.index(min)}")
print(f"{max} est le maximum dans la position {T.index(max)}")

