import sys
import collections
from itertools import permutations

str1 = sys.argv[1]

if len(sys.argv) >= 2:
    str1 = sys.argv[1]

def permString(str):
    perms = [''.join(p) for p in permutations(str)]
    time = 0
    for s in perms:
        if time == 0:
            time = timeCalc(s)
        elif time != 0 and timeCalc(s) < time:
            time = timeCalc(s)
    return(time)
        


def timeCalc(str):
    abc = "abcdefghijklmnopqrstuvwxyz"
    sortStr = str
    stepCounter = 0
    pressCounter = 0
    p1 = p1 = abc.find(str[0])
    time = -1
    for c in sortStr:
        while c != abc[p1]:
            stepCounter += 1
            p1 += 1
            if p1 >= len(abc):
                p1 = 0
        pressCounter += 1
    
        result = stepCounter + pressCounter

        if time == -1:
            time = result
        elif time != -1 and time < result:
            time = result
    return time
        


str3 = permString(str1)

print (str3)
