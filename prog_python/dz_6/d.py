print(" ".join(map(str, map(lambda x: (int(bool(x[0])) + int(bool(x[1]))) % 2, zip(map(int, input().split()), map(int, input().split()))))))
