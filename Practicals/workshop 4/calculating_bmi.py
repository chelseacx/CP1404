
def get_float_value(variable_name, measurement_unit):

    while True:
        try:
            float_value = float(input("Please enter your {} in {}: ".format(variable_name, measurement_unit)))
            break
        except ValueError:
            print("Invalid value!")
    return float_value


print("Body-mass-index calculator, for CP1404")

weight = get_float_value("weight", "kgs")
height = get_float_value("height", "m")

bmi = weight / (height * height)

print("Therefore, your BMI value is: {:.2f}".format(bmi))
print("Thank you!")
