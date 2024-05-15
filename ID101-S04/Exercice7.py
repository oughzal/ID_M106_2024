N = int(input("Entrer la taille de tableau: "))

T = []
for i in range(N):
    j = int(input(f"Entrer l'élément {i+1}: "))
    T.append(j)

for i in range(len(T)):
    if T[i] > 100:
        T[i] *= 1.1

print(f"T: {T}")