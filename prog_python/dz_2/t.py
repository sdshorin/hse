from math import sqrt


def main():
    a = float(input())
    b = float(input())
    c = float(input())
    des = b * b - 4 * a * c
    if des == 0:
        x1 = -b / (2 * a)
        print("{:.6g}".format(x1))
    elif des > 0:
        x1 = float("{:.6g}".format((-b - sqrt(des)) / (2 * a)))
        x2 = float("{:.6g}".format((-b + sqrt(des)) / (2 * a)))
        print("{:.6g} {:.6g}".format(x1, x2))


if __name__ == "__main__":
    main()
