T1 = (100,200,200,400,500,600,200,150,900)
#Afficher le tuple T1
print(T1)
#Afficher le nombre d'occurrence de 200 dans T1
print(T1.count(200))
#Trier T1
T1 =tuple(sorted(list(T1)))
print(T1)

T1 = [100,200,200,400,500,600,200,150,900]
T1.sort() # trier la liste elle-même
L = sorted(T1) # retourner une liste triée de T1