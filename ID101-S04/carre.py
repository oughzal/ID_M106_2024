n = int(input("Donner N :"))
if n%2 ==0 : n +=1
M =[[0 for i in range(n)] for j in range(n)]

# code
for i in range(n):
    for j in range(n):
        print(M[i][j],end="\t")
    print()