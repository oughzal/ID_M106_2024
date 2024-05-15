k, m = map(int, input().split())
array = []
for _ in range(k):
    L=list(map(lambda x : int(x)**2, input().split()))[1:]
    array.append(max(L))
print(sum(array) % m)

