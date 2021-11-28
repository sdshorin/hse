
class Builder:
    def __init__(self):
        self.str = []
        self.sum = 0

    def add_num(self, n):
        self.str.append(f"{n-1}*{n}")
        self.sum += (n - 1) * n

    def get_str(self):
        return "+".join(self.str) + f"={self.sum}"


def main():
    # n = 4
    n = int(input())
    builder = Builder()
    for i in range(2, n + 1):
        builder.add_num(i)
    print(builder.get_str())


if __name__ == "__main__":
    main()
