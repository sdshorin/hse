

def main():
    exit_code = int(input())
    iter = int(input())
    check = int(input())
    print(check_prog(exit_code, iter, check))


def check_prog(exit_code, iter, check):
    if iter == 0:
        if exit_code != 0:
            return 3
        else:
            return check
    elif iter == 1:
        return check
    elif iter == 4:
        if exit_code != 0:
            return 3
        else:
            return 4
    elif iter == 6:
        return 0
    elif iter == 7:
        return 1
    return iter


if __name__ == "__main__":
    main()
