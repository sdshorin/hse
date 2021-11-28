
def main():
    N, throw_q = [int(x) for x in input().split()]
    arr = ["I" for x in range(N)]
    for x in range(throw_q):
        start, finish = [int(x) - 1 for x in input().split()]
        for i in range(start, finish + 1):
            arr[i] = "."
    print("".join(arr))


if __name__ == "__main__":
    main()
