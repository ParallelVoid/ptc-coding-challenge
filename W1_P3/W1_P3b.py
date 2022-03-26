import sys

n = float(sys.argv[1])

if n <= 1000000000.0 and n >= 0.0:
    area = (n/4.0)*(n/4.0)
    print("%.1f") % area
else:
    print("There is no fence")
