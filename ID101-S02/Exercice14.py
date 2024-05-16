from math import sqrt
a= float(input("a : "))
b= float(input("b : "))
c= float(input("c : "))
d= b*b - 4*a*c
if d>0:
    x1=(-b + d**0.5)/(2*a)
    x2=(-b - sqrt(d))/(2*a)
    print(f"Deux solutoin x1={round(x1,2)} et x2={round(x2,2)}")
elif d==0:
    x1=-b/(2*a)
    print(f"une seule solution x={round(x1,2)}")
else:
    print("Pas de solution dans l'ensemble R")

