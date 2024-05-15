T = [1,2,1,1,30,2,3,6,0,6]
for i in range(len(T)):
    for j in range(i+1, len(T)):
        if T[i] == T[j]:
            T[j] = 0
print(f"T: {T}")