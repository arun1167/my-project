the_count=[1,2,3,4,5]
frutis=['apple','orange','avagardo','gwava','banana','jackfruit']
change=[1,'pennies',2,'dimes',3,'quarters']
# This first kind of for loop go through the list

for number in the_count:
	print "This is count %d" %number

# same as above
for fruit in frutis:
	print "A fruit of type: %s" %fruit

# also we can go through mixed list too
# we ae going to use %r becuase we d'nt know waht is it

for i in change:
	print "I got %r" %i

# we can build list first from empty list

elements=[]

# now use range from count 0 to 5

for i in range(0,6):
	print "Adding %d to the list" 
	p=int(raw_input("> "))
	elements.append(p)
# now we can print them out too

for i in elements:
	print "elements was : %d" %i



