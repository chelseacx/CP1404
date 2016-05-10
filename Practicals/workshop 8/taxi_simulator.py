from taxi import Taxi
from silverservicetaxi import SilverServiceTaxi

print("Let's drive!")

bill = 0
taxi = None
taxiList = [Taxi("Limo", 100), Taxi("Prius", 100), SilverServiceTaxi("Hummer", 200, 3.5)]

menuSelection = input("q)uit, c)hoose taxi, d)rive"
                      "\n>>> ")

while menuSelection != "q":

    if menuSelection == "c":

        print("Taxis available:")
        for i, taxi in enumerate(taxiList):
            print("{} - {}, fuel={}, odo={}, ${:.2f}/km, {}km on current fare".format(i, taxi.name, taxi.fuel, taxi.odometer, Taxi.price_per_km, taxi.total_distance))

        taxiSelection = input("Choose taxi: ")
        taxi = taxiList[int(taxiSelection)]

        print("Bill to date: ${:.2f}".format(bill))
        menuSelection = input("q)uit, c)hoose taxi, d)rive"
                              "\n>>> ")

    if menuSelection == "d":

        taxi.start_fare()
        driveDistance = input("Drive how far? ")
        taxi.drive(driveDistance)
        print("That trip cost you ${:.2f}".format(taxi.get_fare()))
        bill += taxi.get_fare()

        print("Bill to date: ${:.2f}".format(bill))
        menuSelection = input("q)uit, c)hoose taxi, d)rive"
                              "\n>>> ")

    else:
        print ("Invalid option")
        print("Bill to date: ${:.2f}".format(bill))
        menuSelection = input("q)uit, c)hoose taxi, d)rive"
                              "\n>>> ")

print("Total trip cost: ${:.2f}".format(bill))
print("Taxis are now:")
for i, taxi in enumerate(taxiList):
    print("{} - {}, fuel={}, odo={}, ${:.2f}/km, {}km on current fare".format(i, taxi.name, taxi.fuel, taxi.odometer,
                                                                              Taxi.price_per_km, taxi.total_distance))