n=int(input("entrer la valeur de n : "))
S = 0
for i in range(1,n+1):
    S += 1/i #S = S + 1/i
print("la somme =",round(S,2))