def estPremier(N:int):
    if N in (1, 2):
        return True
    for i in range(2, N - 1):
        if N % i == 0:
            return False
    return True

print(estPremier(11))
print(estPremier(7))
print(estPremier(4))