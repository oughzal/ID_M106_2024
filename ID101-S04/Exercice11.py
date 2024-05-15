T = [5,8,20,13,16,8,10,9,14,12]
nbAdmis = 0
for e in T:
    if e>=10:
        nbAdmis +=1
nbAdmis = len([e for e in T if e >=10])
nbAdmis = len(list(filter(lambda e: e>=10,T)))
print(f"Le nombre des étudiants admis est {nbAdmis}")