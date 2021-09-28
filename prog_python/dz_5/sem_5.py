



def counter_decorator(original_func):
	def func(*args, **kwargs):
		func.counter += 1
		original_func(*args, **kwargs)
		print(original_func.__name__, func.counter)
	func.counter = 0
	return func

@counter_decorator
def hello():
	print("Helo!")




hello()
hello()
hello()
hello()
hello()
hello()
hello()
hello()
hello()
hello()
hello()




