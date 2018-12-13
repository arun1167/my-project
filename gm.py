def bed_room():
	print " This is interior room of my house"
	print " Very decorative"
	print " Well furnished "
	print " Glad that this is part of my family"
	print " Every family have corner where love to sit and enjoy anything"

def bed_room_parents():
	print " This belongs to our parents"
	print " Ths room is full of books"
	print " This room os full of musco casette"
	print " This is total natelazia"
	print " This have a one bathroom also "
	print " So...that's is very interesting thing in this room"

def kitchen():
	print " The place of secret fire"
	print " Where all the apetite comes to end"
	print " We have very advanced kitchen"
	print " I also know how to cook"
	print " This is amazing to cook in the kitchen"

def drawing_room():
	print " This is our drawing room"
	print " It is full of memory"
	print " We have TV over there"
	print " I like to watch not anymore"
	print " Oh!! this is good  place to relax"

def my_room():
	print " It is spare room on the quarter"
	print " My all personnel stuff is stored over there"
	print " My mother do prayer to god also over there"
	print " I like to sleep over there"

print "***************************************"
print " This is the place where the program start run"
print "***************************************"
print " Eneter your choice"
ch=int(raw_input("> "))

if ch==1:
	bed_room()
elif ch==2:
	bed_room_parents()
elif ch==3:
	kitchen()
elif ch==4:
	drawing_room()
elif ch==5:
	my_room()
else:
	print " Total looser !!"
	exit(0)
