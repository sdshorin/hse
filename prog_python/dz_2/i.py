

def main():
    last_num = int(input())
    accum = 0
    while last_num != 0:
        current_num = int(input())
        if current_num > last_num:
            accum += 1
        last_num = current_num
    print(accum)


if __name__ == "__main__":
    main()
