import car

# A file to show my 2 cars by importing multiple classes from a module by importing
# the whole module. The 2 classes are Car and Electric Car
my_beetle = car.Car("Volkswagen", "Beetle", 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar("Tesla", "Roadster", 2016)
print(my_tesla.get_descriptive_name())