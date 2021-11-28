

from math import sqrt


def main():
    a = int(input())
    b = int(input())
    c = int(input())

    p = (a + b + c) / 2
    S = sqrt(p * (p - a) * (p - b) * (p - c))
    if S.is_integer():
        print(int(S))
    else:
        print(round(S, 6))


if __name__ == "__main__":
    main()
