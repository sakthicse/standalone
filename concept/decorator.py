def div(a,b):
	print(a/b)

def smart(fun):
	def innter(a,b):
		if a < b:
			a,b =b,a
		return fun(a,b)
	return innter
@smart
def div(a,b):
	print(a/b)

# div = smart(div)

div(2,8)