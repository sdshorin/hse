def main():
    task = set(range(1, int(input()) + 1))
    line = input()
    while line != "HELP":
        nums = set(map(int, line.split()))
        # if len(task) / 2 < len(nums):
        cross = task & nums
        if len(cross) > len(task) / 2:
            print("YES")
            task = cross
        else:
            print("NO")
            task -= nums
        line = input()
    print(*sorted(list(task)))


if __name__ == "__main__":
    main()
