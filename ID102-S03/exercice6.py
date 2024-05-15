N = int(input("Donner un nombre : "))
S = 0
for i in range(1,N+1):
    S = 10**i + S
print("La Somme S = ", S)