t = float(input("Donner la température de l'eau :"))
if t <=0 :
    print("Solide")
elif t < 100:
    print("Liquide")
else:
    print("Gaz")