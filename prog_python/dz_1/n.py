def main():
    rub = int(input())
    cop = int(input())
    quantity = int(input())
    rub *= quantity
    cop *= quantity
    print(rub + cop // 100, cop % 100)


if __name__ == "__main__":
    main()
