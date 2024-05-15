L = [1,2,3,2,4,2]
#compter le nombre des occurences d'un valeur
print(L.count(0))
#Trouver l'indice
print(L.index(2,2))
index = -1
for i in range(L.count(2)):
    index = L.index(2,index+1)
    print(index)
# trier
L = [4,2,3,1]
L.sort()
print(L)
L = [4,2,3,1]
L2 = sorted(L)
print(f"L :{L}")
print(f"L2 :{L2}")
#Inverser un list
L = [1,2,3,4]
L.reverse()
print(f"L :{L}")
L = [1,2,3,4]
L2 = list(reversed(L))
print(f"L :{L}")
print(f"L2 :{L2}")

groupe = "ID101"
L = list(groupe)
print(f"L :{L}")
X = 12345
L = list(str(X))
print(f"L :{L}")

L = list(range(10))
print(f"L :{L}")
L2 = L[2:6]
print(f"L2 :{L2}")
L2 =L[3:9:2]
print(f"L2 :{L2}")
L2 =L[3:-2]
print(f"L2 :{L2}")
L2=L[-1:-3:-1]
print(f"L2 :{L2}")
L2 = L[:-2]
L2=L[4:]
L2 = L[-1::-1]
print(f"L2 :{L2}")

L = list(range(10))
for e in L:
    print(e,end=",")
for i in range(len(L)):
    print(L[i],end=", ")

