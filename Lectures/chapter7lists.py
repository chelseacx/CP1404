#Creating a fixed list, and reading out the list
name_list = ['Jenny', 'Alice', 'Tom']
print(name_list[0])
print(name_list[2])
print(name_list[-1])

# Creating an empty list for user to populate the data
user_input_list = [] #create empty list
counter = 0
while True:
    user_input = input("Enter value {} : ".format(counter)) #obtain user input
    counter += 1

    if user_input == "q": #quit the while loop if it's q
        break

    user_input_list.append(user_input) # add the data to the list

print(user_input_list)

output_file = open("user.txt", "w")
print(name_list, file=output_file)
print(user_input_list, file=output_file)
output_file.close()