#I will be using Counter

from collections import Counter
import math

def sort_substring(s):
    sub_str = []
    n = len(s)

    for i in range(n):
        for j in range(i+1, n+1):
            #print(s[i:j])
            sub_str.append(''.join(sorted(s[i:j])))
    return sub_str

def nCr(n,r):
    f = math.factorial
    if r>n:
        return 0

    return f(n)/f(r)/f(n-r)

def sherlockAnagrams(s):
    sub = sort_substring(s)
    same_elements = Counter(sub).values()

    ans = 0

    for i in same_elements:
        ans += nCr(i, 2)

    return int(ans)

if __name__=="__main__":
    q = int(input())
    for i in range(q):
        s = input()
        res = sherlockAnagrams(s)
        print(res)




