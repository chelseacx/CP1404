x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

menu = "\n1. Show the even numbers from " + str(x) + " to " + str(y) \
       + "\n2. Show the odd numbers from "\
       + str(x) + " to " + str(y) + "\n3. Show the squares from " + str(x) + " to " + str(y) + "\n4. Exit the program"

print(menu)
choice = input("\n>>> ")

while choice != "4":

    if choice == "1":
        if x%2 == 0:
            for i in range(x, y+1, 2):
                print(i, end=" ")
        else:
            for i in range(x+1, y+1, 2):
                print(i, end=" ")

    elif choice == "2":
        if x%2 == 0:
            for i in range(x+1, y+1, 2):
                print(i, end=" ")
        else:
            for i in range(x, y+1, 2):
                print(i, end=" ")

    elif choice == "3":
        for i in range(x, y+1):
             print(i*i, end=" ")

    else:
        print("Invalid menu choice")

    print(menu)
    choice = input("\n>>> ")

print("Finished")