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

x = len(num_ordered)/2
output = num_ordered[x] + num_ordered[x-1]


print(output)
