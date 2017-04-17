def func1():
	print(s)
	
s = "Hello World"
func1()

#What we think it'll return: error
#Why: s is defined outside of the function, and not an argument within the function.
# This actually does print Hello World because if the function 
# doesn't find any variables in the local scope it looks for variables 
# in the global scope