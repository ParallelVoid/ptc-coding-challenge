import sys
import math

with open(sys.argv[1]) as file:
    lines = []
    for line in file:
        lines.append(line)

cordinates = []

for x in range(0, 3):
    nums = lines[x].split()
    cordinates.append(nums[0])
    cordinates.append(nums[1])
    if len(nums) > 2:
        cordinates.append(nums[2])
   
    

cord1X = int(cordinates[0])
cord1Y = int(cordinates[1])
speed1 = int(cordinates[2])

cord2X = int(cordinates[3])
cord2Y = int(cordinates[4])
speed2 = int(cordinates[5])

cord3X = int(cordinates[6])
cord3Y = int(cordinates[7])


if cord1X <= 1000000 and cord1X >= -1000000 and cord2X <= 1000000 and cord2X >= -1000000 and cord1Y <= 1000000 and cord1Y >= -1000000 and cord2Y <= 1000000 and cord2Y >= -1000000 and cord3Y <= 1000000 and cord3Y >= -1000000 and cord3X <= 1000000 and cord3X >= -1000000 and speed1 <= 10000 and speed1 >= -10000 and speed2 <= 10000 and speed2 >= -10000:
    rise1 = (cord1Y * cord1Y) - (cord3Y * cord3Y)
    run1 = (cord1X * cord1X) - (cord3X * cord3X)
    slope1 = math.sqrt(rise1 + run1)
    time1 = slope1/speed1


    rise2 = (cord2Y * cord2Y) - (cord3Y * cord3Y)
    run2 = (cord2X * cord2X) - (cord3X * cord3X)
    slope2 = math.sqrt(rise2 + run2)
    time2 = slope2/speed2

    if time1 > time2:
        print ("Callie")
    elif time1 <= time2:
        print ("Hailey")
