def main():
    h = int(input())
    speed = int(input())
    back = int(input())
    print((h - back - 1) // (speed - back) + 1)


if __name__ == "__main__":
    main()
