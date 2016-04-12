LOWER = 10
UPPER = 50

def get_number(lower,upper):

    while True:
        try:
            print("Enter a number({}-{}):".format(lower,upper))
            number = int(input(">>>"))
            if number > UPPER:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid number!")

get_number(LOWER, UPPER)