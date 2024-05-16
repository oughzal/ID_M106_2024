a = float(input("Entrer la valeur de a: "))
b = float(input("Entrer la valeur de b: "))
c = float(input("Entrer la valeur de c: "))

if a == b + c:
    print(f"{a}={b}+{c}") # f-String
elif b == a + c:
    print(b, ' = ', a, ' + ',c)
elif c == a + b:
    print(c, ' = ', a, ' + ',b)
else:
    print("Aucun de ces nombre est la somme des deux autres")