# Créer un dictionnaire D avec les information ....
D = {"nom" : "AKIL","âge" : 18,"ville" : "Benimellal"}
# Ajouter la clé "profession" avec la valeur "technicien" au dictionnaire D
D["profession"] = "technicien"
# modifier la valeur associée à la clé ville à "rabat"
D["ville"] = "rabat"
#Supprimer la clé âge du dictionnaire
del D["âge"]
#Afficher toutes les valeur
print(list(D.values()))
#Afficher les clé
print(list(D.keys()))
#Afficher les entrées
print(list(D.items()))
#Afficher le dictionnaire
print(D)

