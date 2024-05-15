n = int(input("donner N : "))
F = 1
for i in range (1,n+1):
    F *= i #F=F*i
print(n,"! = ",F,sep="")
print(f"{n}! = {F}")