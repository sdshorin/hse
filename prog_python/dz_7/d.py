
def main():
    occured_nums = set()
    for num in map(int, input().split()):
        if num in occured_nums:
            print("YES")
        else:
            print("NO")
            occured_nums.add(num)


if __name__ == "__main__":
    main()
