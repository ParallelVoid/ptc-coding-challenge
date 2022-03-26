import sys

input = sys.argv[1]
num = ""
word = ""
num_total = 0

for l in range (0, len(input)):
    c = input[l]
    if c.isdigit():
        num += c
    elif c.isalpha():
        n = int(num) 
        if n >= 0 and n <= 100000:
            word += (c * n)
        if num != "":
            num_total += n
            num = ""

if (num_total >= 0) and (num_total<= 1000000):
    print(word)
else:
    print ("The word is too large or too small")
    