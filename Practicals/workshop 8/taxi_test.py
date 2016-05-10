from taxi import Taxi


prius = Taxi("Prius 1", 100, 1.20)
prius.drive(40)
print(prius)
print("Current fare is: ${:.2f}".format(prius.get_fare()))

prius.start_fare()
prius.drive(100)
print(prius)
print("Current fare is: ${:.2f}".format(prius.get_fare()))

