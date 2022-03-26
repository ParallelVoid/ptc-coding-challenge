import sys

class Pod:
    def __init__(self, index, teleport, time):
        self.index = index
        self.teleport = teleport
        self.time = time

def f2(start, end):
    result = ""
    for i in range(start, end):
        result += str(i)
    return result

def f1(start, end):
    result = []
    p1 = start+1
    while p1 <= end-1:
        p2 = p1
        while p2 <= end:
#            print("p1=",p1,"p2=",p2)
            v = str(start)
            v += f2(p1, p2)
            v += str(end)
            p2 += 1
#            print("v=",v)
            result.append(v)
        p1 +=1
    return result


def is_valid(c, pods):
    for i in range(0, len(c)):
        s = c[i]
        pod = pods[ int(s)-1 ]
        if i > 0:
            prev_s = c[i-1]
            prev_pod = pods[int(prev_s)-1]
            if pod.index-1 != prev_pod.index and prev_pod.teleport != pod.index:
                return False
    return True

def is_time(c, pods):
    time = 0
    for i in range(0, len(c)):
        s = c[i] #char
        pod = pods[ int(s)-1 ]
        print("pod[", s, "]=", pod.index, pod.teleport, pod.time)
        time += pod.time
        print (time)
    return time
    #     if i > 0:
    #         prev_s = c[i-1]
    #         prev_pod = pods[int(prev_s)-1]
    #         if pod.index-1 != prev_pod.index and prev_pod.teleport != pod.index:
    #             return False
    # return True

with open(sys.argv[1]) as file:
    lines = []
    for line in file:
        lines.append(line)

n = int(lines[0])

pods = []

for i in range (1, n+1):
    x = lines[i].split()
    print(x)
    pods.append(Pod(i, int(x[0]), int(x[1])))


# pods.append(Pod(1,3))
# pods.append(Pod(2,5))
# pods.append(Pod(3,0))
# pods.append(Pod(4,0))
# pods.append(Pod(5,5))



plist = f1(1, n)
plist = list(dict.fromkeys(plist))


minTime = n
for p in plist:
    
    if is_valid(p, pods):
        time = is_time(p, pods)
        print(p, "Time=", time)
        if time < minTime:
            minTime = time

    print("")

print(minTime)