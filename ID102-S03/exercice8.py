N= int (input("Donner un nombre : "))
F = 1
for i in range (1,N+1):
    F = F * i
print(N,"! = ", F)