#défintion d'un fonction (procédure + fonction)
def sayHello(nom:str):
    print(f"Hello {nom}")

def carre(n:int):
    return n*n

def somme(a=2,b=3,c=4):
    return a+b+c
print(somme(1,2,3)) # positionnel
print(somme(c=1,a=2,b=3)) # mot-clé
print(somme(1,2)) # valeur par défaut
print(somme()) # valeur par défaut
print(1,2,3,4,5,6)

def somme2(*numbers):
    return sum(numbers)
print(somme2(1,2,3,4))

