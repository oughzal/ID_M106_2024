# définition d'un fonction ( fonction + procédure)
def max(a,b): # a,b : paramètres (formels)
    if a > b:
        return a
    else:
        return b
def sayHello():
    print("Hello!")

print(max(1,2)) # 1,2 : Argument (effectif)

def somme(a,b=10):
    return a+b
print(somme(2,9)) # a = 2 , b = 9
print(somme(b=7,a=4)) 
print(somme(6)) # a = 6 ; b = 10

def Ecrire(*arg):
    for a in arg:
        print(a,end="")

Ecrire("la somme est ",somme(1,2)," et ...",1,2,4)


