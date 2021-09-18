
def main():
	n = int(input())
	last_fac = 1
	_sum = 0
	for i in range(1, n + 1):
		last_fac *= i
		_sum += last_fac
	print(_sum)

if __name__ == "__main__":
	main()
