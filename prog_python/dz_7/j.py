def main():
    a_1, a_2, b_1, b_2 = map(int, input().split())
    if a_1 > a_2:
        a_1, a_2 = a_2, a_1
    if b_1 > b_2:
        b_1, b_2 = b_2, b_1
    if a_1 <= b_1 and b_1 <= a_2:
        ans = min(a_2 - b_1 + 1, b_2 - b_1 + 1)
    elif b_1 <= a_1 and a_1 <= b_2:
        ans = min(b_2 - a_1 + 1, a_2 - a_1 + 1)
    else:
        ans = 0
    print(ans)


if __name__ == "__main__":
    main()
