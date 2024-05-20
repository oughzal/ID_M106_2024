T = [1,2,3,4,5,6,7,8]
S = sum(T) # sum = somme
M = S/len(T) # len : nombres d'élements de T
P = 1
for e in T:
    P *= e # P = P * e
print(f"La somme est {S}")
print(f"Le produit est {P}")
print(f"La moyenne est {M}")