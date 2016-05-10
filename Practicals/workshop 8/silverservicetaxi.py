from taxi import Taxi

class SilverServiceTaxi(Taxi):

    flagfall = 4.50
    price_per_km = 0

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        SilverServiceTaxi.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        return SilverServiceTaxi.price_per_km * self.current_fare_distance + SilverServiceTaxi.flagfall




