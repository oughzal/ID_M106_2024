def partieEntiere(n:int):
    i = 0
    while i <= n:
        i += 1
    return i-1
def partieEntiere2(n:int):
    return int(str(n).split(".")[0])

print(partieEntiere(9.777))
print(partieEntiere2(9.777))
