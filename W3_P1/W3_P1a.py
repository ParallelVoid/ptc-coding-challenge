import sys
import math

input = sys.argv[1]
num = int(input[0: -1])
if input[-1] == "!":
    ans = math.factorial(num)
    print(ans)
else:
    print("There is no factorial")