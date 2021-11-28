

def distance(x_1, y_1, x_2, y_2):
    return ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5


def IsPointInCircle(x, y, x_c, y_c, r):
    return distance(x, y, x_c, y_c) <= r


def main():
    x = float(input())
    y = float(input())
    x_c = float(input())
    y_c = float(input())
    r = float(input())
    if IsPointInCircle(x, y, x_c, y_c, r):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
