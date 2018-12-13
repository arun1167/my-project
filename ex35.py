from sys import exit
# define first function
def gold_room():
	print "This room is full of gold. How much you take ?"
	next=raw_input("> ")
	if "0" in next or "1" in next:
		how_much=int(next)
	else:
		dead("Man, learn to type number")
	if how_much<50:
		print "Nice, you are not greedy !! you win"
		exit(0)
	else:
		dead("You greddy basterd!")
# defin second function
def bear_room():
	print "This room os for bear"
	print "The bear has a bunch of honey"
	print "The fat bear is in front of another door"
	print "How are you going to move the bear"
	bear_moved = False
# write while loop for interactive input
	while True:
		next=raw_input("> ")
		if next=="take honey":
			dead("The bear looks at you then slaps your face off.")
		elif next=="taunt bear" and not bear_moved:
			print "the bar has moved from the door . You can go through it now"
			bear_moved = True
		elif next=="taunu bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off. ")
		elif next=="open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means"
# define third function
def cthulhu_room():
	print "Here you see the great evil Cthulhu"
	print "He, it, whatever stares at you  and you go insane"
	print "Do you flee  for your life or eat your head?"
	next=raw_input("> ")
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was testy!")
	else:
		cthulhu_room()
# define fourth function
def dead(why):
	print why, "Good Job!"
	exit(0)
# define first fucntion where the program flow start.
def start():
	print "You are in a dark room"
	print "There is a door in right and left"
	print "Which one do you take?"

	next=raw_input("> ")
	if next=="left":
		bear_room()
	elif next=="right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()