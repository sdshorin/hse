
def main():
    s = input()
    new_s = ""
    for char in s:
        new_s += char + "*"
    print(new_s[:-1])


if __name__ == "__main__":
    main()
