N = 100
while N <10 or N > 20:
    N = int(input("Donner un nombre : "))
    if N < 10:
        print("Plus grand")
    if N > 20:
        print("Plus petit")