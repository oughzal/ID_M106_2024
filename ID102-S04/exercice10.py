T = [1,-2,7,-8,5,-10,20,-4,0,30]
Np = 0
Nn = 0
for e in T:
    if e>= 0:
        Np += 1
    else:
        Nn +=1
Np = len([e for e in T if e>=0]) # Méthode 2
Nn = len([e for e in T if e<0]) # Méthode 2
print(f"Le nombre des positifs est {Np} et le nombre des négatifs est {Nn}")