#Remplir le tableau
n = int(input("Donner le nombre des éléments : "))
T =[]
for i in range(n):
    v = float(input(f"Donner T[{i}] : "))
    T.append(v)
 #Augmenter de x le tableau
x = float(input("Donner x : "))
for i in range(len(T)):
    T[i] += x
#Afficher le tableau
print(f"T : {T}")