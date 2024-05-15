n = int(input("Entrer N: "))
i=2
while n % i != 0 and i < n:
    i += 1
if i == n:
    print(n, " est un nombre premier")
else:
    print(n, " n'est pas un nombre premier")