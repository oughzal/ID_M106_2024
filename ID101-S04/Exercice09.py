T = [13,12,19,15,7,8,11,20,15,10]
S = sum(T)
M = S / len(T)
nb = 0 
for e in T:
    if e >= M:
        nb +=1
nb = len([e for e in T if e >= M])
L = len(list(filter(lambda e : e>=M, T)))