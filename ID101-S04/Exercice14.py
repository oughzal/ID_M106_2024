T = [1,2,3,4,5,6,7,8,9,10]
TP = []
for i in T:
    if i % 2 == 0:
        TP.append(i)
TP =[i for i in T if i % 2 == 0]
TP = list(filter(lambda x : x%2==0, T))
TI = []
for i in T:
    if i % 2 != 0:
        TI.append(i)
TI =[i for i in T if i % 2 != 0]
print(f"TP: {TP}")
print(f"TI: {TI}")