name_file = open("name.txt", "r")

print("Your name is {}.".format(name_file.readline()))

name_file.close()