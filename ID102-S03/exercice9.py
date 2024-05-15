N = int(input("Donner N : "))
nb = 0
while N != 0:
    print(N % 10,end=" , ")
    N = N // 10
    nb = nb + 1
print("ce nombre ce compose de ", nb , " chiffres")