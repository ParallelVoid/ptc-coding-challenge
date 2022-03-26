import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

if ((num1 <= int(1000)) & (num2 <= int(1000))):
    print(num1 + num2)
else:
    print('Scores are too large')
