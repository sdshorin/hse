
from decimal import Decimal

def main():
	n = int(input())
	x = Decimal(input())
	result = Decimal(0)
	while n >= 0:
		current_a = Decimal(input())
		if n > 0:
			result = (result + current_a) * x
		else:
			result += current_a
		n -= 1
	result = round(result, 2)
	print(result.normalize())


if __name__ == "__main__":
	main()

