
def main():
    s = input()
    first_pos = s.find("h")
    last_pos_pos = s.rfind("h")
    if first_pos == -1:
        return
    elif first_pos == last_pos_pos:
        return
    else:
        print(s[:first_pos + 1] + s[first_pos +
                                    1:last_pos_pos] * 2 + s[last_pos_pos:])


if __name__ == "__main__":
    main()
