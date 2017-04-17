def func2():
	global s
	print(s)
	s = "hello hello"
	print(s)
	
def func1():
	s = "hi hi"
	print(s)

s = "Hello World"
func2()
print(s)


#will print hello world then hello hello then hello hello again 