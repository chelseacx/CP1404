try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
1.     When will a ValueError occur?

        When an invalid input is entered.
        In this case, it will occur when a non-integer is entered
        such as a character or float.

2.     When will a ZeroDivisionError occur?

        When the user enters the integer 0 as a denominator as numbers cannot be
        divided by 0.

3.   Could you change the code to avoid the possibility of a ZeroDivisionError?

        Only run the fraction line if denominator != 0

"""