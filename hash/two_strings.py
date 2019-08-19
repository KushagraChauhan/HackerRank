
def two_strings(s1, s2):
    if len(set(s1) & set(s2)) >= 1:
        print("YES")

    else:
        print("NO")

if __name__=="__main__":
    q = int(input())
    for q_itr in range(q):
        s1 = input()
        s2 = input()
        two_strings(s1, s2)

