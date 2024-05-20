# Remplir le tableau
n = int(input("Donner le nombre des élémets du tableau : "))
T = []
for i in range(n):
    v = int(input(f"Donner T[{i}] :"))
    T.append(v)

#Augementer d'un valeur X
X = int(input("Donner la valeur du X : "))

for i in range(len(T)):
    T[i] += X # T[i] = T[i] + x

T = [e+X for e in T] # avancé
map(T,lambda a : a +X ) # avancé
#afficher le tableau
print(f"T : {T}")