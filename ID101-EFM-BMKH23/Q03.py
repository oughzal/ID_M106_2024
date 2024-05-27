L = [31,5,"EFM","DRBK",[2,0,2,3],0]
print(L[-4:-1])
print(L[::2]) # [P:D:P] : P=début, d=Fin, P=1
print(L[2:5:1])
print(L[-len(L):len(L)]) # len(L)=6 -> L[-6:6]

#Afficher la longeur de la list L
print(len(L))
#insérer la chaîne "Digital" à l'indice 4 de la liste L
L.insert(4,"Digital")
print(L)
#Supprimer la sous Liste [2,0,2,3] de la liste L
# del L[5]
if L.count([2,0,2,3])>0:
    L.remove([2,0,2,3])
for i in range(L.count([2,0,2,3])):
    L.remove([2,0,2,3])
print(L)