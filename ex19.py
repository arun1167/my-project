def cheese_and_crackers(cheese_count,box_of_crackers):
	print "You have %d cheese" %cheese_count
	print "You have %d crackers" %box_of_crackers
	print "man that's enough for party"
	print "Get a blanket\n"

print "We can give function number directly"
cheese_and_crackers(20,30)

print "Or we can use varaible from the script"
amount_of_cheese=30
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can do inside math to"
cheese_and_crackers(10 + 20,5 + 6)

print "We can combine two variable and do math:"
cheese_and_crackers(amount_of_cheese+300,amount_of_crackers+400)