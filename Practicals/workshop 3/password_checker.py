
import string

MAX_LENGTH = 15
MIN_LENGTH = 5
SPECIAL_CHAR = True

instructions = """
Please enter a valid password
Your password must be between 5 and 15 characters, and contain:
	1 or more uppercase characters
	1 or more lowercase characters
	1 or more numbers
	and 1 or more special characters:  !@#$%^&*()_-=+`~,./o'[]\<>?O{}|
"""
print(instructions)



def lengthCheck(password):
    """Checks the length"""
    if MIN_LENGTH <= len(password) <= MAX_LENGTH:
        valid = True
    else:
        valid = False
    return valid

def upperCaseCheck(password):
    """Checks for an upper case letter"""
    for char in password:
        if char in string.ascii_uppercase:
            valid = True
            break
        else:
            valid = False
            continue
    return valid

def lowerCaseCheck(password):
    """Checks for a lower case letter"""
    for char in password:
        if char in string.ascii_lowercase:
            valid = True
            break
        else:
            valid = False
            continue
    return valid

def numberCheck(password):
    """Checks for a number"""
    for char in password:
        if char in string.digits:
            valid = True
            break
        else:
            valid = False
            continue
    return valid

def specialCharCheck(password):
    """Checks for a special character"""
    for char in password:
        if char in string.punctuation:
            valid = True
            break
        else:
            valid = False
            continue
    return valid

def passwordChecker(password):
    """Checks validity of password"""
    if SPECIAL_CHAR:
        if lengthCheck(password) and upperCaseCheck(password) and lowerCaseCheck(password) and numberCheck(password) and specialCharCheck(password):
            valid = True
        else:
            valid = False
    else:
        if lengthCheck(password) and upperCaseCheck(password) and lowerCaseCheck(password) and numberCheck(password):
            valid = True
        else:
            valid = False
    return valid


password = input("> ")
valid = passwordChecker(password)

while not valid:
    print("Invalid password!")
    password = input("> ")
    valid = passwordChecker(password)


print("Your {} character password is valid: {}".format(len(password), password))



"""
    for char in password:
        if char in string.ascii_lowercase:
            break

    for char in password:
        if char in string.digits:
            break

    for char in password:
        if char in string.punctuation:
            break
"""




