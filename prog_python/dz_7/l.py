
def parse_phone(phone: str):
    clear_phone = ""
    phone = phone.strip()
    for chr in phone:
        if chr.isdigit():
            clear_phone += chr
    if len(clear_phone) == 7:
        clear_phone = "495" + clear_phone
    if len(clear_phone) == 11:
        clear_phone = clear_phone[1:]
    return clear_phone


def main():
    with open("input.txt") as f:
        new_phone = parse_phone(f.readline())
        while True:
            line = f.readline()
            if not line:
                break
            if new_phone == parse_phone(line):
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    main()
