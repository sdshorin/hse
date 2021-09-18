
def get_number(num, pos):
	if pos != 0:
		num = num // 10 ** pos
	return num % 10

def main():
	num = int(input())
	diff = abs(get_number(num, 0) - get_number(num, 3)) +\
			abs(get_number(num, 1) - get_number(num, 2))
	print(diff + 1)

if __name__ == "__main__":
	main()

