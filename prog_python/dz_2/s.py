
from decimal import Decimal


def main():
    n = Decimal(input())
    _sum = Decimal(1)
    while n > 1:
        _sum += 1 / (n * n)
        n -= 1
    _sum = round(_sum, 5)
    print(_sum.normalize())


if __name__ == "__main__":
    main()
