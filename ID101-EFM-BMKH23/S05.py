#Créer le Dictionnaire
D = {"nom":"AKIL","âge":18,"ville":"Benimellal"}
#Ajouter la clé "profession" avec valeur "technicien"
D["profession"] = "technicien" # Ajouter au dictionnaire
#modifier la ville à "Rabat"
D["ville"] = "Rabat"
#Supprimer la clé "âge"
del D["âge"]
#Afficher les valeurs ( pas les clé)
print(D.values())
for v in D.values():
    print(v)
