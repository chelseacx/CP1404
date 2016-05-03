import sys

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
print()

tariff = int(input("Which tariff? 11 or 31:"))
dailyUse = float(input("Enter daily use in kWh: "))
billingDays = int(input("Enter number of billing days: "))

if tariff == 11:
    tariff = TARIFF_11
elif tariff == 31:
    tariff = TARIFF_31

bill = dailyUse * tariff * billingDays
bill = "{0:.2f}".format(bill)

print()
sys.stdout.write("Estimated bill: $")
sys.stdout.write(str(bill))