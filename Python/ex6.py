x = "there are %d types of people." %10
binary = "binary"
doNot = "don't"
y = "those who know %s and those who %s."%(binary,doNot)

print x
print y

print "I said: %r." %x
print "I also said: '%s'." %y

hilarious = False
jokeEvaluation = "Isn't that joke so funny?! %r"
print jokeEvaluation % hilarious
w = "This is the left side of"
e = "a string with a right side"

print w+e