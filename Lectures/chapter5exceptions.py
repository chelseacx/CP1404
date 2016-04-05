try:
    print("1")
    input_file = open("chapter5unknown.txt","r")

    print("2")
    input_file.readline()

    print("3")
    input_file.close()

    print("4")

except ValueError:
    print("The value is problematic")

except FileNotFoundError:
    print("The file is not found")


try:
    number = int(input("Enter sth:"))
    print(10/number)

except ValueError:
    print("Value error")

except ZeroDivisionError:
    print("ZeroDivisionError")

except:     #this catches all other errors
    print("All the rest")

print("Finish")
