import sys

with open(sys.argv[1]) as file:
    lines = []
    for line in file:
        lines.append(line)

n =lines[0]
nums = []

if ((int(n) >= 0) & (int(n) <= 10000)):
    for x in range(1, int(n)+1):
        l = lines[x].split()
        num1 = int(l[0])
        num2 = int(l[1])

        if ((num1 <= int(100000)) & (num2 <= int(100000))):
            nums.append(num1+num2)
        else:
            print('Scores are too large')

listLength = len(nums)
listNum1 = int(nums[0])
listNum2 = int(nums[1])

for y in range(0, listLength):
    if (int(nums[y]) < listNum1) & (int(nums[y]) > listNum2):
        listNum2 = nums[y]

print (listNum2)
