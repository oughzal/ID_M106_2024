L = list(range(20))
L2= L[4:11]
print(L2)
L3 =L[2:12:2]
print(L3)
L4 = L[-3:-1]
print(L4)
L5 = L[-4:]
print(L5)
L6 =L[-1:-4:-1]
print(L6)
L7=L[:5]
print(L7)
L7=L[-1::-1]

print(L7)

L1 = [1,2,3]
L2 = [4,5,6]
L3 = L2 + L1
print(L3)

#parcourir une list
L=list(range(10))
for e in L:
    print(e,end=", ")
print()
for i in range(len(L)):
    print(L[i],end=", ")