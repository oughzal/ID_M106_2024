#Remplir le tableau
n = int(input("Donner le nombre des éléments : "))
T =[]
for i in range(n):
    v = float(input(f"Donner T[{i}] : "))
    T.append(v)

S = sum(T)
M = S/n
nb = 0
for e in T :
    if e >= M :
        nb +=1
NM = [e for e in T if e>=M]
nb = len(NM)
print(f"La somme est {S}")
print(f"La moyenne est {M}")
print("Le nombre des notes supérieur à M est {nb}")