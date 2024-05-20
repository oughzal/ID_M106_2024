def miroire(n):
    inv = 0
    while n!=0:
        inv = inv*10 + n%10
        n //= 10
    return inv
def miroire2(n):
    s = str(n)[-1::-1]
    return int(s)
print(miroire(1234))
print(miroire2(1234))