import sys

input = sys.argv[1]
c = input[-1]
n = int(input[0: -1])

if ((n >= 0) and (n <= 10000)):
    str = ""
    for l in range(0, n):
      str = str + c

    print(str)

else:
    print("Number is too large")
