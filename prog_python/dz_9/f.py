
def get_next_cell_state(arr, i, j):
    live_sum = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if (x == i and y == j) or x < 0 or y < 0 or\
                    x >= len(arr) or y >= len(arr):
                continue
            if arr[x][y]:
                live_sum += 1
    if live_sum < 2:
        return 0
    elif live_sum > 3:
        return 0
    elif live_sum == 2:
        return arr[i][j]
    elif live_sum == 3:
        return 1


def next_live_step(arr):
    next_arr = []
    for i in range(len(arr)):
        next_arr.append([])
        for j in range(len(arr)):
            next_arr[i].append(get_next_cell_state(arr, i, j))
    return next_arr


def print_arr(arr):
    for line in arr:
        print(" ".join(list(map(str, line))))


def main():
    n, time = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    for i in range(time):
        arr = next_live_step(arr)
    print_arr(arr)


if __name__ == "__main__":
    main()
