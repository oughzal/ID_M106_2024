# // Remplissage du Tableau
Voyelles = ['a','e','i','o','u','y']



# Voyelles[0] = 'a'
# Voyelles[1] = 'e'
# Voyelles[2] = 'i'
# Voyelles[3] = 'o'
# Voyelles[4] = 'u'
# Voyelles[5] = 'y'
Voyelles = []
Voyelles.append('a')
Voyelles.append('e')
Voyelles.append('i')
Voyelles.append('o')
Voyelles.append('u')
Voyelles.append('y')
# //Afficher le tableau
# pour i de 0 à 5 Faire
#         Ecrire(Voyelles[i],",")
# finpour
print(Voyelles)
for v in Voyelles:
    print(v, end=",")
print()
for i in range(len(Voyelles)):
    print(Voyelles[i], end=",")

