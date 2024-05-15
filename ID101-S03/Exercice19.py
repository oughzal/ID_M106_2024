N=int(input("Entrez la valeur de N : "))
m=N
i=1
P=1
while N!=0:
    N=int(input("entrez la valeur de N : "))
    i=i+1
    if m <N:
        m=N
        p=i
print("le max des nombres saisies est",m,"a la position",p)
