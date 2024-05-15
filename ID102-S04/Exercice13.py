T = [1,-5,2,-3,7,8,-9,0,6,11]
TP =[]
TN =[]
for e in T:
    if e>=0:
        TP.append(e)
    else:
        TN.append(e)
#Methode 2
TP =[e for e in T if e>=0]
TN =[e for e in T if e<0]
print(f"T : {T}")
print(f"TP : {TP}")
print(f"TN : {TN}")