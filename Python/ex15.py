from sys import argv

script,filename = argv

txt = open(filename)

print "Here's your file %r:" %filename
print txt.read()

print "Type the filename agin"
fileAgain = raw_input(">")
txtAgain = open(fileAgain)

print txtAgain.read()