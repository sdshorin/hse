

from decimal import Decimal


def main():
    num = Decimal(input())
    if num % 1 == 0.5:
        num += Decimal(0.1)
    print(round(num))


if __name__ == "__main__":
    main()
