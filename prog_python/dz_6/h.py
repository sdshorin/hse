from functools import reduce, partial
from operator import xor

print(" ".join(map(str, list(map(partial(reduce, xor), zip(
    *map(lambda x: map(int, input().split()), range(int(input())))))))))
