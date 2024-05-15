n=int(input("donner un nombre :"))
S=0
print([i for i in range(1,n) if n%i==0])
for i in range(1,n):
    if n%i==0:
       S =S+i
S  = sum([i for i in range(1,n) if n%i==0])
if S ==n:
    print(f"{n} est un nombre parfait")
else:
   print(f"{n} n'est pas un  nombre parfait") 