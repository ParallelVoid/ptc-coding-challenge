import sys
import math

with open(sys.argv[1]) as file:
    lines = []
    for line in file:
        lines.append(line)

n = int(lines[0])

if n >= 0 and n <= 1000000:
    for i in range (1, n + 1):
        num = int(lines[i])
        if num >= 1 and num <= 1000000:
            ans = math.factorial(int(num))
            print(ans)
        else:
            break
else:
    print("The factorial is too large")