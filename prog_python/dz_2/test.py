import unittest


def sort_2(x, y):
    if x >= y:
        return y, x
    else:
        return x, y


def sort_3(x, y, z):
    if x <= y and x <= z:
        return x, *sort_2(y, z)
    elif y <= x and y <= z:
        return y, *sort_2(x, z)
    elif z <= y and z <= x:
        return z, *sort_2(x, y)


def main():
    x1 = int(input())
    y1 = int(input())
    z1 = int(input())
    x2 = int(input())
    y2 = int(input())
    z2 = int(input())
    _main(x1, y1, z1, x2, y2, z2)


def _main(x1, y1, z1, x2, y2, z2):

    x1, y1, z1 = sort_3(x1, y1, z1)
    x2, y2, z2 = sort_3(x2, y2, z2)
    if x1 == x2 and y1 == y2 and z1 == z2:
        print("Boxes are equal")
        return "equal"
    elif x1 <= x2 and y1 <= y2 and z1 <= z2:
        print("first box is smaller than the second one")
        return "box2 bigger"
    elif x1 >= x2 and y1 >= y2 and z1 >= z2:
        print("The first box is larger than the second one")
        return "box1 bigger"
    else:
        print("Boxes are incomparable")
        return "incomparable"


def define(vec_1, vec_2):
    x1, y1, z1 = vec_1[0], vec_1[1], vec_1[2]
    x2, y2, z2 = vec_2[0], vec_2[1], vec_2[2]
    return _main(x1, y1, z1, x2, y2, z2)


class TestDefineBoxes(unittest.TestCase):

    def test_upper(self):
        b1 = (2, 5, 9)
        b2 = (9, 2, 5)
        result = define(b1, b2)
        self.assertEqual(result, "equal")

    def test_b1(self):
        pairs = [((3, 5, 9), (9, 2, 5)),
                 ((2, 15, 10), (9, 2, 5)),
                 ]
        for pair in pairs:
            result = define(*pair)
            self.assertEqual(result, "box1 bigger")

    def test_b2(self):
        pairs = [((9, 2, 5), (3, 5, 9)),
                 ((9, 2, 5), (2, 15, 10)),
                 ]
        for pair in pairs:
            result = define(*pair)
            self.assertEqual(result, "box2 bigger")

    def test_incomparable(self):
        pairs = [((9, 3, 5), (2, 5, 10)),
                 ((9, 2, 5), (1, 15, 10)),
                 ]
        for pair in pairs:
            result = define(*pair)
            self.assertEqual(result, "incomparable")


if __name__ == '__main__':
    unittest.main()
