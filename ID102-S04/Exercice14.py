T = [1,2,3,4,5,6,7,8,9,10]
TP =[] # [2,4,6,8,10]
TI = [] # [1,3,5,7,9]
for e in T:
    if e % 2 == 0:
        TP.append(e) # Ajouter à la fin du tableau
    else:
        TI.append(e)
print(f"T : {T}") # f-string
print("T :",T)
print(f"TP : {TP}")
print(f"TI : {TI}")
