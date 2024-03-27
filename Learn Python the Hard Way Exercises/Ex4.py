
# defines "carrs" variable to give out "100" as tex when used in function
cars = 100

# defines variable
space_in_a_car = 4.0

# same
drivers = 30

# same
passengers = 90

# defines name of variablw and computes value by executing equation of one variable's value minus second variables's value.
cars_not_driven = cars - drivers

# defines variable's value by another variable
cars_driven = drivers

# same as in line 11
carpool_capacity = cars_driven * space_in_a_car

# same as in line 11 but replace simple minus or plus with operators
average_passengers_per_car = passengers / cars_driven


# prints out text, interrupted by insertion of value of one variable
print("There are", cars, "cars available.")

# same as line 27
print("There are only", drivers, "drivers available")

# same as line 27
print("There will be", cars_not_driven, "empty cars today.")

# same as line 27
print("We can transport", carpool_capacity, "people today.")

# same as line 27
print("We have", passengers, "to carpool today.")

# same as line 27
print("We need to put about", average_passengers_per_car, "in each car.")