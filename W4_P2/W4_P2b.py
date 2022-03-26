import sys
import random

# with open(sys.argv[1]) as file:
#     lines = []
#     for line in file:
#         lines.append(line)

n = 4 #####int(lines[0])
cards = ("a 4 b 2").split()
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
        # if i < n - 1:
        #     if cards[i - 1].isalpha() and cards[i + 1].isalpha() and cards[i].isalpha():
        #         if (cards[i - 1].islower() and cards[i + 1].isupper()) or (cards[i - 1].isupper() and cards[i + 1].islower()):
        #             squishy = True
        #         else:
        #             squishy = False

output = []
outputStr = ""

if squishy:
    print("Yes")
    for i in range (0, n):
        if cards[i].isdigit():
            if output[i - 2].islower():
                output.append(chr(random.randint(ord('A'), ord('Z'))))
            elif output[i - 2].isupper():
                output.append(chr(random.randint(ord('a'), ord('z'))))
            elif cards[i - 1].islower():
                output.append(chr(random.randint(ord('A'), ord('Z'))))
            elif card[i - 1].isupper():
                output.append(chr(random.randint(ord('a'), ord('z'))))
        if cards[i].isalpha():
            x = int(cards[i - 1])
            if i < n-1:
                y = int(cards[i + 1])
                if x >= 0 and x <= 9 and y >= 0 and y <= 9 and cards[i].islower():
                    num = random.randint(0, 9)
                    output.append(str(num))
                elif x >= 0 and x <= 9 and y >= 0 and y <= 9 and cards[i].isupper():
                    num = random.randint(0, 9)
                    output.append(str(num))
    for i in range (0, len(output)):
        outputStr += output[i] + " "
    print(outputStr)
else:
    print("False")