
def check_is_free(x, y, arr):
    for i in range(8):
        if arr[i][y]:
            return False
        if arr[x][i]:
            return False
        if 0 <= x - y + i <= 7:
            if arr[x - y + i][i]:
                return False
        if 0 <= y + x - i <= 7:
            if arr[i][y + x - i]:
                return False
    return True


def main():
    arr = [[None for y in range(8)] for x in range(8)]
    is_crossed = False
    for i in range(8):
        x, y = [int(x) - 1 for x in input().split()]
        if not check_is_free(x, y, arr):
            is_crossed = True
        arr[x][y] = True
    if is_crossed:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
