

def distance(x_1, y_1, x_2, y_2):
    return ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5


def main():
    x_1 = float(input())
    y_1 = float(input())
    x_2 = float(input())
    y_2 = float(input())
    x_3 = float(input())
    y_3 = float(input())
    perimetr = distance(x_1, y_1, x_2, y_2) +\
        distance(x_1, y_1, x_3, y_3) +\
        distance(x_2, y_2, x_3, y_3)
    print(f"{perimetr:.10f}")


if __name__ == "__main__":
    main()
