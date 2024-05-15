n=int(input("Donner un nombre : "))
while n<10 or n>20:
    if n<10 :
        print("Plus Grand")
    if n>20:
        print("Plus Petit")
    n=int(input("Donner un nombre : "))