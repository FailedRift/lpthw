#Assigns variables based on car data. 
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passegers_per_car = passengers / cars_driven

#prints the number of cars available. 
print("There are", cars, "cars available" )
#prints the number of drivers available.
print("Thera are only", drivers, "drivers available.")
#prints the number of cars not driven. 
print("There will be", cars_not_driven, "empty cars today.")
#prints the amount of spaces available for car pool. 
print("We can transport", carpool_capacity, "people today.")
#prints the number of passengers for the car pool
print("We have", passengers, "to carpool today.")
#prints the number of people in each car. 
print("We need to put about", average_passegers_per_car, "in each car.")