
def main():
    s = input()
    space_pos = s.find(" ")
    print(s[space_pos + 1:], s[:space_pos])


if __name__ == "__main__":
    main()
