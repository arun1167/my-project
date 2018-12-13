ten_things="Apple Orange Crows Telephone Light Sugar"
print "Wait there's not 10 things in the list, let's fix that."

stuff=ten_things.split(' ')
more_stuff=["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff)!=10:
	next_one=more_stuff.pop()
	stuff.append(next_one)
	print "There are %d itme now " %len(stuff)

print "there we go\n", stuff

print "Let's do some things with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
