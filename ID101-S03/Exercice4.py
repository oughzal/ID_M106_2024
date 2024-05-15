n = int(input("Entrer un nombre : "))
U0 = 0
U1 = 1
# pour i de 2 à N faire
for i in range(2,n+1):
    U2 = U0 + U1
    U0 = U1
    U1 = U2
    print(U2, ", ")
