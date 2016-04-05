guitarFile = open("chapter5guitarList.txt", "r")

guitarList = guitarFile.readlines()

fender = guitarList[0]
gibson = guitarList[1]
line = guitarList[2]

# printing entire list
print ("\n".join(guitarList))

#printing specific lines:
print (gibson)

guitarFile.close()
