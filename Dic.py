#créer un dictionnaire
D ={"A":1,"B":2,"C":3,"D":4}
D2 = {'X':7,'Y':8}
# D.update(D2)
D.update(D2)
print(D)
#Accès ou modifier un élément
print(D["A"])
print(D.get("G",0))
D["C"] = 10
D["E"] = 5 #Ajouter un élément
#parcourir d'un dictionnaire
# for k in D: print(k)
# for k in D.keys() : print(k)
# for v in D.values() : print(v)
# for k,v in D.items() : print(f"{k} : {v}")

personne = {'nom' : 'Dupont' , 'prénom' : 'Jean' , 'age' : 30}
D.update(personne)
print(D)
