#solution without using re
s = input()

print(s.isdigit() and 100000 <= int(s) <= 999999 and 
      sum([s[i] == s[i+2] for i in range(0, 4)]) < 2)