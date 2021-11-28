def main():
    A = int(input())
    B = int(input())
    _max = B * int(not(A // B)) + A * int(not(B // A)) + A * int(not(A - B))
    print(_max)


if __name__ == "__main__":
    main()
