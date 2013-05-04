def add(a,b):
	print "Adding %d + %d "%(a,b)
	return a + b

def subtract(a,b):
	print "subtract %d - %d" % (a ,b)
	return a - b

def multiply(a,b):
	print "multiply %d * %d" % (a,b)
	return a * b
	
def divide(a,b):
	print "divide %d / %d" % (a ,b)
	return a/b

print "Let's do some math with just functins!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d,height: %d, weight: %d,iq: %d "%(age,height,weight,iq)

print "Here is a puzzle"
what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print "that become:",what,"Can you do it by hand?"