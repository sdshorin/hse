
def main():
    s = input()
    first_pos = s.find("f")
    last_pos_pos = s.rfind("f")
    if first_pos == -1:
        return
    elif first_pos == last_pos_pos:
        print(first_pos)
    else:
        print(first_pos, last_pos_pos)


if __name__ == "__main__":
    main()
