numbers_file = open("numbers.txt","r")

total = 0

for line in numbers_file:

    total += int(line)

numbers_file.close()

print (total)
