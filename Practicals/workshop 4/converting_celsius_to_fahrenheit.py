
def get_celsius_value():
    while True:
        try:
            celsius_value = float(input("Enter the Celsius Value: "))
            break
        except ValueError:
            print ("Invalid Input!")
    return celsius_value


print("\nCelsius to Fahrenheit Converter for CP1404\n")

celsius_value = get_celsius_value()

fahrenheit_value = celsius_value * 1.8 + 32

print("Fahrenheit Value: {:,.1f} F".format(fahrenheit_value))