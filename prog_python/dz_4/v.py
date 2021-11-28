
def xanoi(disk, source, target):
    if disk != 1:
        xanoi(disk - 1, source, 6 - source - target)
    print(disk, source, target)
    if disk != 1:
        xanoi(disk - 1, 6 - source - target, target)


def main():
    n = int(input())
    xanoi(n, 1, 3)


if __name__ == "__main__":
    main()
