from collections import defaultdict

def ransom_note(magazine, note):
    dict1 = defaultdict(int)
    for word in magazine:
        dict1[word] += 1
    for word in note:
        if dict1[word] == 0:
            print("No")
            return False
        dict1[word] -= 1
    print("Yes")
    return True

if __name__=="__main__":
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    ransom_note(magazine, note)
