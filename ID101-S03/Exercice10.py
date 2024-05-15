n = int(input("Entrer n: "))
Inv = 0
print(f"l'inverse de {n} est {str(n)[-1::-1]}")
while n != 0:
    Inv = Inv*10 + n % 10
    n //= 10
print(f"L'inverse est {Inv}")
