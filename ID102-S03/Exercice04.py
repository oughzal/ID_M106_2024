N = int(input("Donner N : "))
U0 = 0
U1 = 1
for i in range(2,N+1):
    U2 = U1 + U0
    U0 = U1
    U1 = U2
    print(U2, end=", ")