import sys

num = int(sys.argv[1])

if num >= 0 and num <= 100:
    letter = sys.argv[2]

    str = ""
    for n in range(0, num):
      str = str + letter

    print(str)

else:
    print("Number is too large")    
