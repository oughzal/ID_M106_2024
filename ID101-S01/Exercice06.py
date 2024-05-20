from datetime import datetime
now = datetime.now().year
# CETTE_ANNEE = 2024
CETTE_ANNEE = datetime.now().year
# // Entree 
annee = int(input("Donner l'année de naissance : "))
# //Traitement
age = CETTE_ANNEE - annee
# //Sortie
print("vous avez " , age , " ans")
print("votre age est ", age ," ans")