
def print_num_deffer():
    n = int(input())
    is_printed = False
    if n != 0:
        is_printed = print_num_deffer()
    if int(n ** 0.5)**2 == n and n != 0:
        print(n, end=" ")
        is_printed = True
    return is_printed


def main():
    if not print_num_deffer():
        print(0)
    else:
        print()


if __name__ == "__main__":
    main()
