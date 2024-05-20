HT = float(input("Donner le prix HT : "))
cat = input("Donner la catégorie (A,B,C) : ")
if cat=='A'or cat=='a':
    TVA=0.07
elif cat.lower()=='b':
    TVA =0.2
else :
    TVA =0.25  
TTC = (1+TVA)*HT
print("TTC : ", TTC)