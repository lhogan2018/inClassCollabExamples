def func1(s):
	print(s)
	
s = "Hello World"
func1()

#What we think it'll return: error
#Why: s is defined outside of the function, and not an argument within the function.