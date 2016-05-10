from guitar import Guitar


print("My guitars!")

guitarList = []
guitarNum = 0
name = input("Name: ")
while name != "":

    year = input("Year: ")
    cost = input("Cost: $")

    guitarList.append(Guitar(name, year, cost))
    guitar = guitarList[guitarNum]
    print(guitar.__str__() + " added.")
    guitarNum += 1
    name = input("Name: ")


print("\nThese are my guitars:")

for i, guitar in enumerate(guitarList):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    print(("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_string)))
