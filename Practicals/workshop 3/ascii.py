LOWER = 10
UPPER = 100

print("Enter a number ({}-{}):".format(LOWER, UPPER))

lower = int(input("Lower Number: "))
upper = int(input("Upper Number: "))
print("DEC  CHAR")
for i in range(lower, upper+1):
    if i==100:
        print("{}{:>4}".format(i, chr(i)))
    else:
        print("{}{:>5}".format(i,chr(i)))