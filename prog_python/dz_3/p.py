
def main():
    for i in range(10, 100):
        if 2 * (i % 10) * (i // 10) == i:
            print(i)


if __name__ == "__main__":
    main()
