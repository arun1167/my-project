# Assign value to the varaibles
cars=100
space_in_a_car = 4
drivers = 30
passangers = 90
# calculation started
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity=cars_driven * space_in_a_car
average_passanger_per_car = passangers / cars_driven
# varaibel output
print "**************************"
print "There are",cars,"cars available"
print "There are only",drivers,"drivers available"
print "There will be ",cars_not_driven,"empty cars today"
print "We are transport",carpool_capacity,"people capacity"
print "We have",passangers,"to carpool only"
print "we need to put about",average_passanger_per_car,"in each car"