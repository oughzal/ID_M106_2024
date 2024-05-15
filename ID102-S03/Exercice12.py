N = int(input("Donner N :"))
S=0
if N % 2 ==0:
    for i in range(2,N+1,2):
        S = S + i
else:
    for i in range(1,N+1,2):
        S = S + i
print("La somme est ", S)

S= 0
for i in range(N,0,-2):
    S = S + i
print("La somme est ", S)