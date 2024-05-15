from random import randint

T = []
for i in range(100):
    T.append(randint(1,6))
T = [randint(1,6) for i in range(100)]
F = [ 0 for i in range(6)]
for e in T:
    F[e-1] += 1
print(f"F : {F}")

for i in range(6):
    F[i] = T.count(i+1)
F = [T.count(i+1) for i in range(6)]