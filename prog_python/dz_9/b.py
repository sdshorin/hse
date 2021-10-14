
DEBUD_DRAW_MODE = False


def print_move(disk, source, target):
    if DEBUD_DRAW_MODE:
        print(source - 1, target - 1)
    else:
        print(disk, source, target)


def xanoi(disk, source, target):
    if disk != 1:
        xanoi(disk - 1, source, 6 - source - target)
    print_move(disk, source, target)
    if disk != 1:
        xanoi(disk - 1, 6 - source - target, target)


def xanoi_main(disk, source, target):
    if disk <= 0:
        return
    if disk != 1:
        xanoi(disk - 1, source, 6 - source - target)
    print_move(disk, source, target)
    if disk > 3:
        xanoi(disk - 3, 6 - source - target,  source)
    if disk > 2:
        print_move(disk-2, 6 - source - target, target)
    if disk > 3:
        xanoi_main(disk-3, source, 6 - source - target)


def main():
    # n = 4
    n = int(input())
    if n % 2:
        xanoi_main(n, 1, 2)
    else:
        xanoi_main(n, 1, 3)


if __name__ == "__main__":
    main()
