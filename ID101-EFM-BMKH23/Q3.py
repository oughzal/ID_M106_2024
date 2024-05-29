L = [31,5,'EFM','drbk',[2,0,2,3],0]

print(L[-4:-1]) #  ['EFM,'drbk',[2,0,2,3]]
print(L[::2]) # [31,'EFM',[2,0,2,3]]
print(L[2:5:1]) # ['EFM','drbk',[2,0,2,3]]
print(L[-len(L):len(L)]) # [-6:6] [31,5,'EFM','drbk',[2,0,2,3],0]

d = 0
f = len(L)
p = 1
L2 = L[-1:0:-1] # inverser une liste

#Q3.2
L = [31,5,'EFM','drbk',[2,0,2,3],0]
# Afficher la longueur de la liste L
print(len(L))
#Inserer la chaîne 'digital' à l'indice 4 de la liste L
L.insert(4,'digital')
# Supprimer la sous-list [2,0,2,3]
L.remove([2,0,2,3])
del L[5]
#Déplacer 'drbk' à l'indice 1
L.insert(1,L[3])
del L[4]


print(L)

