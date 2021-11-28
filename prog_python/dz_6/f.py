from itertools import accumulate

print("\n".join(map(str, accumulate(
    range(1, int(input()) + 1), lambda x, y: x * y, initial=1))))
