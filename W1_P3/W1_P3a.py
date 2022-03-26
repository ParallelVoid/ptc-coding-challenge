import sys

with open(sys.argv[1]) as file:
    lines = []
    for line in file:
        lines.append(line)
        
n = 0
if len(lines) > 0 and int(lines[0]) <= 100 and int(lines[0]) >= 0: 
    n = int(lines[0])
else:
    print("There is no fence")

nums = []
if len(lines) > 1:  
    nums = lines[1].split()
    nums = list(map(int, nums))

num_ordered = sorted(nums)
string = ""

for l in range(0, n):
    number = num_ordered[l]
    if number >= -100000 and number <= 100000:
        string = string + str(number) + " "
    else:
        string = "The fence is too large"
        break


print(string)
