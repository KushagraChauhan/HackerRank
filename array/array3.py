#this is the new year chaos question

def minBribes(q):
    moves = 0
    q = [p-1 for p in q]

    for i,p in enumerate(q):
        if p-i > 2:
            print("Too chaotic")
            return

        for j in range(max(p-1, 0), i):
            if q[j] > p:
                moves += 1

    print(moves)
    return

if __name__=="__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        q = [int(n) for n in input().split()]
        minBribes(q)
