
def calc_rectangle_area(length, width):
    area = length * width
    return area

def get_float_value(variable_name):

    while True:
        try:
            float_value = float(input("Enter value of {}: ".format(variable_name)))
            break
        except ValueError:
            print("Invalid value!")
    return float_value

print("\nRectangle Area Calculator for CP1404\n")

rectangle_length = get_float_value("Rectangle length")
rectangle_width = get_float_value("Rectangle width")
rectangle_area = calc_rectangle_area(rectangle_length, rectangle_width)

print("Area of Rectange is: {}".format(rectangle_area))