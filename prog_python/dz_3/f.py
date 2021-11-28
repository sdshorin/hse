
def main():
    s = input()
    pos = s.find("f")
    if pos == -1:
        print(-2)
    elif s[pos + 1:].find("f") == -1:
        print(-1)
    else:
        print(1 + pos + s[pos + 1:].find("f"))


if __name__ == "__main__":
    main()
