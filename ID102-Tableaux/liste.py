L = [1,1.2,"id102",False]
L =[]
#Ajouter à la fin
L.append(2)
L.append(1)
L.append(3) #[1,2,3]
#insérer dans une position
L.insert(1,40) #[1,4,2,3]
L.insert(0,15) #[5,1,4,2,3]
#etendre une list
L.extend([9,4,80])
L = L + [99,3] #[5, 1, 4, 2, 3, 6, 7, 8, 9, 10]
#supprimer
L.remove(1) # supprimer par valeur
L.pop(2) # supprimer par postion
del L[0]
#Compter
print(L.count(10))
print(len(L))

#trier
#L.sort()
L2 = sorted(L,reverse=True)


#inverser la liste
L.reverse()
L3 = list(reversed(L))

print(L[3])
L[0] =1000
print(L)