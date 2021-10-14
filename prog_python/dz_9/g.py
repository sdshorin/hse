
def main():
    sum_arr = [0 for i in range(9)]
    while True:
        num = int(input())
        if num <= 0 or num >= 10:
            break
        sum_arr[num - 1] += 1
    print(" ".join(map(str, sum_arr)))


if __name__ == "__main__":
    main()
