def estParfait(N):
    s =0
    for i in range(1,N):
        if N%i==0:
            s+=i

    return s==N
def estParfait(N):
    return N == sum([e for e in range(1,N) if N%e == 0])

print(estParfait(6))
print(estParfait(28))
print(estParfait(392))