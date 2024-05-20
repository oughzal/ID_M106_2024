#Remplir le tableau
n = int(input("Donner le nombre des éléments : "))
T =[]
for i in range(n):
    v = float(input(f"Donner T[{i}] : "))
    T.append(v)
#incrémenter de 10%
for i in range(len(T)):
    if T[i]>=100:
        T[i] *= 1.1
#Afficher le tableau
print(f"T : {T}")
