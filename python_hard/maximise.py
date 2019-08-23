from itertools import product

k, m = map(int, input().split())
N =[]
for _ in range(k):
    l = input().split()
    l = list(map(int, l))
    l = l[1:]
    N.append(l)

results = map(lambda x: sum(i**2 for i in x)%m, product(*N))
print(max(results))