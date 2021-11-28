import functools
import operator

print(functools.reduce(operator.mul,
                       (map(lambda x: x ** 5, map(int, input().split())))))
