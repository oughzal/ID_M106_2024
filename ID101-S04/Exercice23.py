T1 = [1,3,5,8,9,0,2,10,12,13]
T2 = [1,13,5,8,29,0,24,10,15,13]
#méthode 1
nb = 0
for i in range(len(T1)):
    if T1[i] == T2[i] :
        nb += 1
print(f"Le nombre des éléments égaux est {nb}")
#méthode 2
nb = len([T1[i] for i in range(len(T1)) if T1[i] == T2[i]])
print(f"Le nombre des éléments égaux est {nb}")