c = input("Entrer un caractère : ")
if 'A' <= c <= 'Z': 
    print(f"{c} est une majuscule")
elif c>='a' and c<='z':
    print(f"{c} est une minuscule")
elif '0' <= c <= '9':
    print(c, " est un chiffre")
else:
    print(f"{c} est un symbole")