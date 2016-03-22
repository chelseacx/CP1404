temperature = float(input("Enter the temperature today: "))

if temperature > 35:
    print(temperature > 35)
    print("We are bbq-ed") #printed if temperature > 35 gives True
elif temperature > 33:
    print("Don't go outdoor.")
else:
    print("It's not too bad")

print("Always printed")
