Voyelles =[]
#Voyelles =['a','e','i','o','u','y']
# // Remplissage du tableau
# Voyelles[0] = 'a'
Voyelles.append('a')
# Voyelles[1] = 'e'
Voyelles.append('e')
# Voyelles[2] = 'i'
Voyelles.append('i')
# Voyelles[3] = 'o'
Voyelles.append('O')
# Voyelles[4] = 'u'
Voyelles.append('u')
# Voyelles[5] = 'y'
Voyelles.append('y')

# //afficher le tableau
# pour i de 0 à 5 Faire
#  Ecrire(Voyelles[i], ", ") 
# finpour
for c in Voyelles:
    print(c,end=", ")
print()
for i in range(len(Voyelles)):
    print(Voyelles[i],end=", ")