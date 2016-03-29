quantity = int(input("Enter the number of items: "))

while quantity < 0:
    print("Invalid number of items!")
    quantity = int(input("Enter the number of items: "))

cost = float(input("Enter the shipping cost per item: "))

total = quantity * cost

if total > 100:
    total = total * 0.9

print("The total shipping cost is ${:.2f}".format(total))