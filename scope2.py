def func1():
	s = "hi hi"
	print(s)

s = "Hello World"
func1()
print(s)

# We think this will return hi hi \n Hello World because the function will find
# the local s ("hi hi") before it finds the global s ("Hello World") but the
# print(s) function will only find the global s ("Hello World")