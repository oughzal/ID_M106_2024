L = [1,2,3] # list : mutable (modifiable)
L.append(4)
T = (1,2,3) # tuple : immutable (non modifiable)
D ={"k":1,2:3} # Dictionnaire paires (key,value)
Stagiaire = {"nom":"Achraf", "age":20,"ville":"Khénifra"}
print(Stagiaire)

L = [1,2,1,2,3,3,4]
s = set(L) # set : ensemble une liste sans duplication (double)
print(s)

# chaîne (String)
s = "ifrastructure digitale 102"
print(s.upper()) # majuscrule
print(s.lower()) # miniscule
print(s.title()) # l 1er caractère de chaque mot en majuscule
print(s.capitalize()) # le 1er caractère en maj
print(s.islower) # True si tous les lettres en miniscule
print(s.split())
ip ="192.168.1.20"
print(ip.split("."))
