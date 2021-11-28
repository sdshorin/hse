import itertools
from collections import namedtuple


def main():
    arr = [int(x) for x in input().split()]
    Num = namedtuple("Num", ["num", "id"])
    maximums = []
    maximums_minuses = []
    minimums = []
    id = 0
    for x in arr:
        if x >= 0:
            maximums.append(Num(x, id))
            maximums.sort(reverse=True, key=lambda x: x[0])
            if len(maximums) > 3:
                maximums.pop()
        else:
            minimums.append(Num(x, id))
            minimums.sort(key=lambda x: x[0])
            if len(minimums) > 3:
                minimums.pop()
            maximums_minuses.append(Num(x, id))
            maximums_minuses.sort(reverse=True, key=lambda x: x[0])
            if len(maximums_minuses) > 3:
                maximums_minuses.pop()
        # print(maximums, maximums_minuses, minimums)
        id += 1
    useful_nums = maximums + maximums_minuses + minimums
    used_id = []
    useful_nums_processed = []
    for num in useful_nums:
        if num.id in used_id:
            continue
        used_id.append(num.id)
        useful_nums_processed.append(num.num)
    variants = list(itertools.combinations(useful_nums_processed, 3))
    # print(variants)
    variants.sort(reverse=True, key=lambda arr: arr[0] * arr[1] * arr[2])
    print(" ".join([str(x) for x in variants[0]]))


if __name__ == "__main__":
    main()
