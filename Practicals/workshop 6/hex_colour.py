colourCodes = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378"}


colourName = input("Enter a colour name: ")
while colourName != "":
    if colourName in colourCodes:
        print("{} is {}.".format(colourName, colourCodes[colourName]))
        colourName = input("\nEnter a colour name: ")
    else:
        print("\nColour does not exist.\n")
        hexCode = input("Please enter the hexadecimal colour code for the new colour: ")
        colourCodes[colourName] = hexCode
        colourName = input("\nEnter a colour name: ")