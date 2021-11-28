
def main():
    n = int(input())
    print("+___ " * n)
    for i in range(n):
        print(f"|{i + 1} / ", end="")
    print()
    print(r"|__\ " * n)
    print("|    " * n)


if __name__ == "__main__":
    main()
