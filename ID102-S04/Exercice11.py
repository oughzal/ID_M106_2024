T = [16,8,10,13,19,17,9,5,16,1]
# nombre des Admis
nbAdmis = 0
for e in T:
    if e>=10:
        nbAdmis += 1
#méthode 2
nbAdmis = len([e for e in T if e>=10])

print(f"Le nombre des admis est {nbAdmis}")
