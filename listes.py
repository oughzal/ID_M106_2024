L =[1,2,3]
#Ajouter un élément à la fin de la liste
L.append(5) #[1,2,3,5]
#insérer un élement à une postion de la liste
L.insert(3,4) #[1,2,3,4,5]
#Ajouter plusieurs éléments à la fin de la liste
L.extend([6,7]) #[1,2,3,4,5,6,7]
L = L + [8,9] #[1,2,3,4,5,6,7,8,9]
#Supprimer le premier element correspondant à une valeur
L.remove(2) #[1,3,4,5,6,7,8,9]
# supprimer et retourner l'élement à un indice
frst = L.pop() #[3,4,5,6,7,8,9]
frth = L.pop(3) #[3,4,5,7,8,9]
del L[0] #[4,5,7,8,9]
del L # supprimer la liste de la mémoire


