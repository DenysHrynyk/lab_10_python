from Bicycle import Bicycle


def main():
    print("Number_of_wheels_in_Bike = ", Bicycle.number_of_wheels())

    pride_rockteady_bicycle = Bicycle(21, 16, 120, "Pride",
                                      "urban", "steel", "Ukraine")
    marin_riftZone_bicycle = Bicycle(10, 15, "Marin", "mountain")

    salsa_jorneyman700lc = Bicycle("Salsa", "Touring")

    pride_rockteady_bicycle.__str__()
    marin_riftZone_bicycle.__str__()
    salsa_jorneyman700lc.__str__()


if __name__ == '__main__':
    main()

