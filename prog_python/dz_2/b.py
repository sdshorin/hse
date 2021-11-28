def main():
    x = int(input())
    y = int(input())
    z = int(input())
    window_x = int(input())
    window_y = int(input())
    min_a = 0
    min_b = y
    if x <= y and x <= z:
        min_a = x
        if y <= z:
            min_b = y
        else:
            min_b = z
    elif y <= x and y <= z:
        min_a = y
        if x <= z:
            min_b = x
        else:
            min_b = z
    elif z <= y and z <= x:
        min_a = z
        if y <= x:
            min_b = y
        else:
            min_b = x
    if min_b < min_a:
        min_b, min_a = min_a, min_b
    if window_y < window_x:
        window_x, window_y = window_y, window_x
    if window_x >= min_a and window_y >= min_b:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
