class Bicycle:
    number_of_wheels = 2

    def __init__(self, number_of_gears=None, mass=None,maximum_load=None, name_of_the_manufacturer=None, type_of_bike=None,
                 frame_material=None, producing_country=None):
        self.number_of_gears = number_of_gears
        self.mass = mass
        self.maximum_load = maximum_load
        self.name_of_the_manufacturer = name_of_the_manufacturer
        self.type_of_bike = type_of_bike
        self.frame_material = frame_material
        self.producing_country = producing_country

    def __str__(self):
        print ("\nNumber_of_gears =", self.number_of_gears,
               "\nMass_of_bicycle =", self.mass,
               "\nMaximum_load =", self.maximum_load,
               "\nName_of_the_manufacturer =", self.name_of_the_manufacturer,
               "\nType_of_bike =",self.type_of_bike,
               "\nFrame_material =", self.frame_material,
               "\nProducing_country =", self.producing_country, "\n")

    @staticmethod
    def number_of_wheels():
        return Bicycle.number_of_wheels

    def __del__(self):
        print("Destroying an object")