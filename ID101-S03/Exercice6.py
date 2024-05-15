n = int(input("Entrer N: "))
S = 0
for i in range(1,n+1):
    S += 10 ** i
print(f"la somme est: {S}")