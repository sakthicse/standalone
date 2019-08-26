def generator_fun(n):
	i=1
	while i<n:
		yield i
		i=i+1
values = generator_fun(10)
print(values)
for j in values:
	print(j)