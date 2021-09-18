
from decimal import Decimal, getcontext

def main():
	pr_int = int(input())
	pr = Decimal(str(pr_int // 100) + f".{ pr_int % 100:02}" )
	rub = int(input())
	cop = int(input())
	years = int(input())
	money = rub * 100 + cop
	while years > 0:
		money += money * pr
		years -= 1
		money = int(money)
	print(f"{money // 100} {money % 100}")


if __name__ == "__main__":
	main()

