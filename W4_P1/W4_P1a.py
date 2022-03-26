import sys
import collections

str1 = sys.argv[1]

def alphabets(str1):
    abc = "abcdefghijklmnopqrstuvwxyz"
    b = {b: 0 for b in abc}
    sb = collections.OrderedDict(sorted(b.items()))
    for i in range (0, len(str1)):
        sb[str1[i]] += 1
    x=""
 
    for key, val in sb.items():
        x+=str(val) + " "

    return x


str2 = alphabets(str1)
print(str2)
