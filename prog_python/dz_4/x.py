
import math


def find_squares(n, deep):
    if deep <= 0:
        return False
    for i in range(1, int(n ** 0.5) + 1):
        if n == i ** 2:
            return [i]
        if n > i ** 2:
            squares_arr = find_squares(n - i ** 2, deep - 1)
            if squares_arr:
                return [i] + squares_arr
        else:
            break
    return False


def main():
    n = int(input())
    squares = find_squares(n, 4)
    if squares:
        print(" ".join(str(i) for i in squares))
    else:
        print(0)


if __name__ == "__main__":
    main()
