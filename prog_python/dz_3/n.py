
LINE = "123456789"


def main():
    n = int(input())
    for i in range(n):
        print(LINE[:i + 1])


if __name__ == "__main__":
    main()
