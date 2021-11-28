
def C(n, k):
    if n == k or k == 0:
        return 1
    return C(n - 1, k - 1) + C(n - 1, k)


def main():
    n = int(input())
    k = int(input())
    print(C(n, k))


if __name__ == "__main__":
    main()
