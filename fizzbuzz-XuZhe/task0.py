i = 0
while i<=100:
	i = i + 1
	if i % 3 == 0:
		if i % 5 == 0:
			print("FizzBuzz")
		else:
			print("Fizz")
	elif i % 5 == 0:
		if i % 3 == 0:
			print("FizzBuzz")
		else:
			print("Buzz")
	else:
		print(i)
