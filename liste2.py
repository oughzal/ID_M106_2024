L =[1,2,6,4,5,6,7,8,9]
#acces à un élément
print(L[1]) # 2
# modifier un élément
L[2] = 3  # [1,2,3,4,5,6,7,8,9]
#découper(slicing) une liste
L2 = L[2:5] # L2 : [3,4,5]
L3 = L[1:6:2] # L3 :[2,4]
L4 =L[:2] # L4 :[1,2]
L5 = L[-1:-3:-1] #[9,8]
#longeur de la liste
print(len(L))
#Concatenation
L1 = [1,2,3] ; L2=[4,5,6]
L3 = L1 + L2 # [1,2,3,4,5,6]
#parcourir d'un liste
for e in L:
    print(e)
for i in range(len(L)):
    print(L[i])