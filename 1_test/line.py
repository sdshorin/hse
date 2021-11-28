class Line:

    def __init__(self, k, b):
        self.k = k
        self.b = b

    def __eq__(self, other):
        return self.k == other.k and self.b == other.b

    def is_parralel(self, other):
        return self.k == other.k and self.b != other.b

    def get_value_for_x(self, x: int):
        return self.k * x + self.b

    def get_intersect(self, other):
        if self == other or self.is_parralel(other):
            return (0, 0)
        xk = self.k - other.k
        yb = -self.b + other.b
        cross_x = float(yb) / xk
        cross_y = self.get_value_for_x(cross_x)
        return cross_x, cross_y


def main():
    x, y = [int(i) for i in input().split()]
    line_1 = Line(x, y)
    x, y = [int(i) for i in input().split()]
    line_2 = Line(x, y)

    if line_1 == line_2:
        print("coincide")
    elif line_1.is_parralel(line_2):
        print("parallel")
    else:
        print("intersect")
        x, y = line_1.get_intersect(line_2)
        if x.is_integer():
            x = int(x)
        if y.is_integer():
            y = int(y)
        print(x, y)


if __name__ == "__main__":
    main()
