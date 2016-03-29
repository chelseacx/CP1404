name = input("Enter name: ")

menu = "(H)ello\n(G)oodbye\n(Q)uit"

print (menu)
choice = input("\n>>> ")

while choice != "Q":

    if choice == "H":
        print("Hello " + name)

    elif choice == "G":
        print("Goodbye " + name)

    else:
        print("Invalid choice")

    print (menu)
    choice = input("\n>>> ")

print("Finished")
