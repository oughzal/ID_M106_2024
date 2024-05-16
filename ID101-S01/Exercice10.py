# //Entree
T =  int(input("Donner le temps en secondes : "))

# //Traitement
H = T // 3600 # H = T DIV 3600
T = T % 3600 # T = T MOD 3600
M = T // 60 # M = T DIV 60
S = T % 60 # S = T MOD 60
print(H,":",M,":",S , sep="")