N = int(input("Donner N : "))
U = 1 
for i in range(1,N+1):
    U = 4*U + 6
print("U", N, " = ", U)