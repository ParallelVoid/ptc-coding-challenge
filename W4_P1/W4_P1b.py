import sys
import collections

str1 = sys.argv[1]


def timetotype(str1):
    abc = "abcdefghijklmnopqrstuvwxyz"
    b = {b: 0 for b in abc}
    ll = len(str1)
    kcount = 0
    ii = 0
    sb=collections.OrderedDict(sorted(b.items()))

    for i in range (0, len(str1)):
        sb[str1[i]] += 1
    # print(sb)
    for key, val in sb.items():
        # print(val)
        if ii >= ll:
            return kcount
        
        if val == 0:
            kcount += 1
        else:
            ii += val
            kcount += val+1
            if ii >= ll:
                return kcount - 1

        
    return kcount


str3 = timetotype(str1)
print (str3)
