T1 = [4,8,7,9,1,5,4,6]
T2 = [7,6,5,2,1,3,7,4]
T3 = []
s=0
for e in T1:
    x=e+T2[s]
    T3.append(x)
    s=s+1

T3 =[]
for i in range(len(T1)):
    x = T1[i] + T2[i]
    T3.append(x)

T3 =[T1[i]+T2[i] for i in range(len(T1)) ]
print(T3)