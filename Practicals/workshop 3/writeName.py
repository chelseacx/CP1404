
name = input("Please enter your name: ")

name_file = open("name.txt","w")
name_file.write(name)
name_file.close()