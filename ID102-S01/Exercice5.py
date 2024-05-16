# //Entrée
N1 = float(input("Donner la valeur de N1 : "))
N2 = float(input("Donner la valeur de N2 : "))
N3 = float(input("Donner la valeur de N3 : "))

# // Traitement
# tmp = N3
# N3 = N1
# N1 = tmp
N1,N2,N3 = N3,N2,N1
# //Sortie
print("N1 : ", N1,"; N2 : ", N2,", N3 : ", N3)