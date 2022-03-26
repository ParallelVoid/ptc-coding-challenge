import sys

with open(sys.argv[1]) as file:
    lines = []
    for line in file:
        lines.append(line)

n =lines[0]

if ((int(n) >= 0) & (int(n) <= 10000)):
    for x in range(1, int(n)+1):
        l = lines[x].split()
        num1 = int(l[0])
        num2 = int(l[1])

        if ((num1 <= int(10000)) & (num2 <= int(10000))):
            print(num1 + num2)
        else:
            print('Scores are too large')

