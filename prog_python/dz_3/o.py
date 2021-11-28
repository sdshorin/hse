
def main():
    start = int(input())
    finish = int(input())
    for num in range(start, finish + 1):
        if str(num) == str(num)[::-1]:
            print(num)


if __name__ == "__main__":
    main()
