
def main():
    start = int(input())
    finish = int(input())
    order = -1 + 2 * int(bool(finish > start))
    for i in range(start, finish + order, order):
        print(i)


if __name__ == "__main__":
    main()
