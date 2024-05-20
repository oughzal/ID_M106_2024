HT= float(input("Donner le prix HT du produit : "))
cat = input("Donner la catégorie du produit (A, B, C) : ")

if cat=='a' or cat=="A":
    TVA=0.07
elif cat.lower()=='b':
    TVA=0.2
else:
    TVA = 0.25

TTC = HT*(1+TVA)
print(f"TTC = {TTC}")