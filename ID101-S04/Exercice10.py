T = [-2,3,-1,5,20,-30,9,5,4,2]
Sp = 0
Sn = 0
for e in T:
    if e>0:
        Sp += e
    else:
        Sn += e
Sp = sum([e for e in T if e>0])
Sn = sum([e for e in T if e<0])

Sp = sum(list(filter(lambda e: e> 0, T)))
Sn = sum(list(filter(lambda e: e< 0, T)))
print(f"la somme des positifs est {Sp}")
print(f"la somme des négatifs est {Sn}")