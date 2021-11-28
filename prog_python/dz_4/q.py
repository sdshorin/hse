
def phib(n):
    if n <= 2:
        return 1
    return phib(n - 1) + phib(n - 2)


def main():
    n = int(input())
    print(phib(n))


if __name__ == "__main__":
    main()
