from itertools import permutations
from functools import reduce, partial
print("\n".join(map(partial(reduce, lambda x, y: x + y), permutations(map(str, range(1, int(input())  + 1))))))
