T =[1,6,8,2,9,0,5,10,11,13]
p = int(input("Donner la position de supression : "))
print(f"T : {T}")
if p>=0 and p<len(T):
    del T[p]
else:
    print("la position de supression n'est pas valide")
print(f"T : {T}")