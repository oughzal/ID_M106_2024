mylist = []
n = int(input("Entrer le nombre des elements: "))
for i in range(n):
    x = int(input(f"Entrer l'element {i+1}: "))
    mylist.append(x)
print(mylist)