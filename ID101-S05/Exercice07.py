# pas de passage par adresse en python
def swap(a,b):
    return b,a # retourner deux valeurs
a = 7
b = 2
a,b = swap(a,b)
print(f"a:{a} ; b:{b}")
