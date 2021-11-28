
def main():
    arr = [int(x) for x in input().split()]
    counted = [0 for x in range(101)]
    for x in arr:
        assert(0 <= x <= 100)
        counted[x] += 1
    elem_to_rewrite = 0
    for i in range(101):
        for j in range(counted[i]):
            arr[elem_to_rewrite] = i
            elem_to_rewrite += 1
    print(" ".join([str(i) for i in arr]))


if __name__ == "__main__":
    main()
