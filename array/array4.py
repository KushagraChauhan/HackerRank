#this is the minimum swap to sort the arrsy

def minSwaps(a):
    n = len(a)
    arrpos = [*enumerate(a)]
    arrpos.sort(key=lambda it: it[1])
    vis = {k: False for k in range(n)}

    ans = 0
    for i in range(n):
        if vis[i] or arrpos[i][0] == i:
            continue

        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arrpos[j][0]
            cycle_size += 1
        if cycle_size > 0:
            ans += (cycle_size - 1)
    print(ans)

if __name__=="__main__":
    n = int(input())
    a = [int(n) for n in input().split()]
    minSwaps(a)