T1 =[4,8,7,9,1,5,4,6]
T2 = [7,6,5,2,1,3,7,4]
#Remplir T3
T3 =[]
for i in range(len(T1)):
    T3.append(T1[i] + T2[i])
#méthode 2
T3 = [T1[i]+T2[i] for i in range(len(T1))]
print(f"T3 : {T3}")
