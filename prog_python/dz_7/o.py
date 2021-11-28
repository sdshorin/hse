
def main():
    sin_q = int(input())
    sin_dict = {}
    for i in range(sin_q):
        a, b = input().split()
        sin_dict[a] = b
        sin_dict[b] = a
    print(sin_dict[input()])


if __name__ == "__main__":
    main()
