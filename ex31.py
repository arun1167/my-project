print "You enter a dark room with two doors. Do you go through  door #1 or door #2 ?"

door=raw_input("> ")

if door=="1":
	print "There's a giant beer eating here chesse cake. What do you do ?"
	print "1. Take the cake."
	print "2. Scream the bear."
###########################
	bear=raw_input("> ")
###########################
	if bear=="1":
		print "The eats your face off. Good Job !"
	elif bear=="2":
		print "The bear eats you logs off. Good Job !"
	else:
		print "Well , doing %s is probably better. Bear runs away." %bear
###########################
elif door=="2":
	print "You stare into the endless abyess at Cthulhu's retina"
	print "1. Blueberries."
	print "2. Yellow jacket clothespies."
	print "3. Understanding resolves yelling melodies."
###########################
	insanity=raw_input("> ")
###########################
	if insanity=="1" or insanity=="2":
		print "Your body servives powered by a mind of jello. Good Job"
	else:
		print "The insanity rots  your eyes into a pool of muck. Good Job"
else:
	print "You stuble around and fall on a knife and die. good Job"
###########################

