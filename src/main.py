class TourPackage:
    def __init__(self, country="", duration=0, price=0.0, number_of_people=0, travel_type=""):
        self.__country = country
        self.__duration = duration
        self.__price = price

        self.number_of_people = number_of_people
        self.travel_type = travel_type

    def get_country(self):
        return self.__country

    def get_duration(self):
        return self.__duration

    def get_price(self):
        return self.__price

    def set_country(self):
        return self.__country
    def set_duration(self):
        return self.__duration
    def set_price(self):
        return self.__price

    def __str__(self):
        return (f"Tour Package to {self.__country}, Duration: {self.__duration} days, "
                f"Price: {self.__price} EUR, Number of people: {self.number_of_people},"
                f" travel type: {self.travel_type}")

    def __repr__(self):
        return (f"Tour Package to {self.__country}, Duration: {self.__duration} days, "
                f"Price: {self.__price} EUR, Number of people: {self.number_of_people},"
                f" travel type: {self.travel_type}")

    def __del__(self):
        print(f"TourPackage to {self.__country} is being deleted")

def main():
    tour1 = TourPackage("Italy", 7, 1200.0, number_of_people=15, travel_type="by ship")
    tour2 = TourPackage("France", 10, 1500.0, number_of_people=30, travel_type="by bus")
    tour3 = TourPackage("Greece", 5, 900.0, number_of_people=10, travel_type="by plane")


    print(tour1)
    print(tour2)
    print(tour3)
    print(repr(tour1))
    print(repr(tour2))
    print(repr(tour3))

main()
