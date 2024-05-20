n = int(input("Entrer n: "))
nb = 0
n2 = n
print(f"{n2} se compose de {", ".join(list(str(n)))} ({len(list(str(n)))} chiffres)")
out = ""
while n != 0:
    out = f"{n%10}, {out}"
    n //= 10
    nb += 1
print(f"{n2} se compose de {out[:-2]} ({nb} chiffres)")
