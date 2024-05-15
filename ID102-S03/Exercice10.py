N = int(input("Donner N : "))
print(str(str(N)[-1::-1]))
inv =0
while N != 0:
    inv = inv*10 + N%10
    N = N // 10
print("L'inverse est ", inv)