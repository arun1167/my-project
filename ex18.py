# this one is like the sscript with argv
def print_two(*args):
	arg1,arg2=args
	print "arg1 : %r  arg2 : %r" %(arg1,arg2)

# ok, that *args is actually pointless , we can  just do this
def print_two_again(arg1,arg2):
	print "arg1 :%r arg2 :%r" %(arg1,arg2)
def print_one(arg1):
	print "arg1 :%r" %arg1


# this just one argument
def print_none():
	print "I got nothing."

print_two("Zed","Show")
print_two_again("Zed","Show")
print_one("First!")
print_none()