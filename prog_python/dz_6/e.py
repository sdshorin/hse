from itertools import accumulate

print(" ".join(map(str, accumulate(map(int, input().split()), lambda x, y: x + y))))