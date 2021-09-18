

from decimal import Decimal

def main():
	num = Decimal(input())
	print(int(num), int(num%1 * 100))


if __name__ == "__main__":
	main()