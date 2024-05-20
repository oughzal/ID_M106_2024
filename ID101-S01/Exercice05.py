# //Entrée
N1 = int(input("Donner la valeur de N1 : "))
N2 = int(input("Donner la valeur de N2 : "))
N3 = int(input("Donner la valeur de N3 : "))
# Traitement
# tmp = N1
# N1 = N3
# N3 = tmp
N1, N3 = N3,N1
# Sortie
print(N1, ", " , N2, ", " , N3)