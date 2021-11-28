

def IsPointInSquare(x, y):
    return abs(x) + abs(y) <= 1


def main():
    x = float(input())
    y = float(input())
    if IsPointInSquare(x, y):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
