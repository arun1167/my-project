# this program is to describe function to 
def add(a,b):
	print "ADDING %d + %d" %(a,b)
	return a+b
def subtract(a,b):
	print "SUBTRACT %d - %d" %(a,b)
	return a-b
def multiply(a,b):
	print "MULTIPY %d * %d" %(a,b)
	return a*b
def divide(a,b):
	print "Divide %d / %d" %(a,b)
	return a/b
###################################
age=add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(100,2)
###################################
print "Age: %d Height:%d Weight:%d IQ:%d" %(age,height,weight,iq)
###################################
# a puzzle for the extra credit,type it in anyway
print "here is a puzzle"
###################################
what=add(age,subtract(height,multiply(weight,divide(iq,2))))

print "That becomes:",what,"Can you do it by hand"


