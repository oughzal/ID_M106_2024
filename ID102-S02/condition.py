a = int(input("Donner A : "))
b = int(input("Donner B : "))
c = int(input("Donner c : "))
if a> b :
    if a > c:
        max = a
    else :
        max=c
else :
    if b> c:
        max = b
    else :
        mac = c
print("max :",max)

note = float(input("donner la note :"))
if note < 0 :
    print("E")
elif note < 10:
    print("R")
elif note<10:
    print("P")
#....
else:
    print("E")

