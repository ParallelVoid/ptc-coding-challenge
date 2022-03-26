import sys

with open(sys.argv[1]) as file:
    lines = []
    for line in file:
        lines.append(line)

n = int(lines[0])
cards = lines[1].split()
squishy = False

if n >= 3 and n <= 100000:
    for i in range (0, n):
        if cards[i - 1].isdigit() and cards[i + 1].isdigit():
            x = int(cards[i - 1])
            if i < n-2:
                y = int(cards[i + 1])
                if x >= 0 and x <= 9 and y >= 0 and y <= 9:
                    if x + y > 5 and cards[i].islower():
                        squishy = True
                    else:
                        squishy = False
        if i < n - 1:
            if cards[i - 1].isalpha() and cards[i + 1].isalpha() and cards[i].isalpha():
                if (cards[i - 1].islower() and cards[i + 1].isupper()) or (cards[i - 1].isupper() and cards[i + 1].islower()):
                    squishy = True
                else:
                    squishy = False

if squishy:
    print("Yes")
else:
    print("False")