T=[-1,1,3,5,-8,0,9,-4,-12,6]
TP=[]
TN =[]
for e in T:
    if e>=0:
        TP.append(e)
    else:
        TN.append(e)
TP =[e for e in T if e>=0]
TN =[e for e in T if e<0]

TP = list(filter(lambda e : e>=0, T))
TN = list(filter(lambda e : e<0, T))
print(f"T : {T}")
print(f"TP : {TP}")
print(f"TN : {TN}")