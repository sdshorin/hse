
def main():
    pow = int(input())
    for i in range(10 ** (pow) - 1, 10 ** (pow - 1) - 1, -2):
        print(i, end=" ")
    print()


if __name__ == "__main__":
    main()
