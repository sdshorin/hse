
def Election(x, y, z):
    return (x and y) or (x and z) or (y and z)


def main():
    x, y, z = map(lambda x: bool(int(x)), input().split())
    print(int(Election(x, y, z)))


if __name__ == "__main__":
    main()
