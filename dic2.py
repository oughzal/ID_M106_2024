D ={"A":10,"B":5,1:5,True:6,2:"v"}
person ={
    'nom':"nom",
    "prenom" :"Ali",
    "age" :20,
    "fonction" :"Stagiaire"
}

for k in D:
    print(k)
for k in D.keys():
    print(k)
for v in D.values():
    print(v)
for k,v in D.items():
    print(f"{k}:{v}")