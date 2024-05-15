T = [1,2,3,4,5,6,7,8,9,10]
v = int(input("Donner la valeur rechechée"))
if v in T :
    print(v,"existe dans T")
else :
    print(v,"n'existe pas dans T")
i = 0
while i < len(T) and T[i]!=v: i +=1