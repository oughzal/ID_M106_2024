T = [i for i in range(1,11)]
v = int(input("Donner la valeur : "))
p = int(input("Donner sa position : "))
if p in range(len(T)):
    T.insert(p,v)
else:
    print("position invalide")