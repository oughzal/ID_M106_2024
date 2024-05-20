#Méthode 1
T = [1,2,3,1,7,1,4,5,2,5,3,8,1,2,3]
L =[]
print(f"T : {T}")
for e in T :
    if e not in L:
        L.append(e)
T = L
print(f"T : {T}")
#méthode 2
T = [1,2,3,1,7,1,4,5,2,5,3,8,1,2,3]
i = 0
while i < len(T) -1:
    j = i+1
    while j < len(T):
        if T[i] == T[j]:
            del T[j]
        j += 1
    i += 1
print(f"T : {T}")
#méthode
T = [1,2,3,1,7,1,4,5,2,5,3,8,1,2,3]
i = 0

while i < len(T) -1 :
    for j in range(T[i+1:].count(T[i])):
        index = T.index(T[i],i+1)
        del T[index]
    i += 1
print(f"T : {T}")