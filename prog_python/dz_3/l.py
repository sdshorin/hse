
def main():
    s = input()
    new_s = ""
    i = 0
    for char in s:
        if i % 3:
            new_s += char
        i += 1
    print(new_s)


if __name__ == "__main__":
    main()
