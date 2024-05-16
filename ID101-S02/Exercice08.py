N = int(input("Donner un nombre : "))
if N==6 :
    print("Le personnage va à droite")
elif N==4 :
    print("Le personnage va à gauche")
elif N==8 :
    print("Le personnage va en haut")
elif N==2 :
    print("Le personnage va en bas")
else:
    print("erreur, le personnage ne bouge pas")

match N: # version 3.10+
    case 6 :
        print("Le personnage va à droite")
    case 4,9:
        print("Le personnage va à gauche")
    case 8:
        print("Le personnage va en haut")
    case 2 :
        print("Le personnage va en bas")
    case _ : #Sinon
        print("erreur, le personnage ne bouge pas")