import sys
import math

with open(sys.argv[1]) as file:
    lines = []
    for line in file:
        lines.append(line)

cordinates = []

for x in range(0, 2):
    nums = lines[x].split()
    cordinates.append(nums[0])
    cordinates.append(nums[1])

cord1 = lines[0].split()
cord2 = lines[1].split()
cord1X = int(cord1[0])
cord1Y = int(cord1[1])
cord2X = int(cord2[0])
cord2Y = int(cord2[1])

if cord1X >= 1000 and cord1X <= -1000 and cord2X >= 1000 and cord2X <= -1000 and cord1Y >= 1000 and cord1Y <= -1000 and cord2Y >= 1000 and cord2Y <= -1000:
    rise = (cord2Y * cord2Y) - (cord1Y * cord1Y)
    run = (cord2X * cord2X) - (cord1X * cord1X)
    slope = math.sqrt(rise+run)

    slope = round(slope, 1)
    print(slope)

else:
    print ("The distance is too large")
