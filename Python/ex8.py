formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ("one","two","three", "four")
print formatter % (True, False , False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
	"I had this thing",
	"that you could type up rigt",
	"but it didn't string",
	"so i said goodnight"
	)