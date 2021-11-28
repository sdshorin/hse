
def pow(a, b):
    if b <= 0:
        return 1
    if b % 2 == 0:
        return(pow(a, b / 2) ** 2)
    else:
        return(a * pow(a, b - 1))


def main():
    a = float(input())
    b = int(input())

    print(f"{pow(a, b):g}")


if __name__ == "__main__":
    main()
