
tariffDictionary = {"TARIFF_11": 0.244618, "TARIFF_31": 0.136928}

print("Electricity Bill Estimator\n")

for k, v in tariffDictionary.items():
    print("Tariff Name: {} \nTariff Price: ${}\n".format(k, v))

tariff = input("Which tariff?\n>>> ")

while tariff not in tariffDictionary.keys():
    print("Invalid tariff.")
    tariff = input("\nWhich tariff?\n>>> ")

use = float(input("Enter daily use in kWh: "))
days = float(input("Enter the number of days in the billing period: "))
price = tariffDictionary[tariff]

bill = price * use * days

print("Estimated bill: ${:.2f}".format(bill))