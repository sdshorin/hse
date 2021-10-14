from itertools import combinations


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    counter = 0
    for triangle in combinations(arr, 3):
        if triangle[2] < triangle[0] + triangle[1]:
            counter += 1
    print(counter)


if __name__ == "__main__":
    main()
