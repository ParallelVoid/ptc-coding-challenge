import sys
import math

input = int(sys.argv[1])

if input >= 1 and input <= 100000:
    for n in range(1, input + 1):
        ans = math.factorial(n)
        print(ans)

else:
    print("The factorial is too large")