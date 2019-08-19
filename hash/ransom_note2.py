from collections import Counter

def ransom_note(magazine, note):
    if (Counter(note) - Counter(magazine)) == {}:
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    ransom_note(magazine, note)
