def isPrim(n:int,L:list):
    for i in L[1:]:
        if n%i == 0:
            return False
    return True
def primList(n:int):
    L =[]
    if(n>=1): L.append(1)
    if(n>=2): L.append(2)
    for i in range(2,n+1):
        if isPrim(i,L):
            L.append(i)
    return L


n = int(input("Donner un nombre : "))
print("prims :",primList(n))