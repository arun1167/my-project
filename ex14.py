from sys import argv

script, user_name = argv
prompt = '> '
print "Hi %s ,I am the %s script" %(script,user_name)
print "I would you like you to ask few questions"
print " %s do you like me "  % user_name

likes = raw_input(prompt)

print "Where do you live %s ?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have"
computer = raw_input(prompt)

print """
Alright, so you  said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer . Nice.
""" %(likes,lives,computer)

