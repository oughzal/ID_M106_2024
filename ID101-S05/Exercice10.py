def fact(n):
    f = 1
    for i in range(1,n+1):
        f *= i
    return f
def fact2(n):
    if n==0 : return 1
    return n* fact(n-1)

print(fact(6))
print(fact2(6))