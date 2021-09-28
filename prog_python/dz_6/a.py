import functools

print(functools.reduce(lambda x, y: y if y % 2 and (y < x or not x % 2)  else x , map(int, input().split())))
