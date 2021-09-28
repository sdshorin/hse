
from collections import namedtuple
from bisect import bisect_left

def main():
	Safe = namedtuple("Safe", ["pos", "num"])
	city_n = int(input())
	city_pos = [int(x) for x in input().split()]
	safe_n = int(input())
	safe = [Safe(int(y), x + 1) for x, y in enumerate(input().split())]
	safe.sort()
	safe_pos = [s.pos for s in safe]
	ans = []
	for city in city_pos:
		closest_1 = bisect_left(safe_pos, city)
		closest_2 = closest_1 - 1

		if 0 <= closest_1 < len(safe_pos) and 0 <= closest_2 < len(safe_pos):
			if abs(safe_pos[closest_1] - city) < abs(safe_pos[closest_2] - city):
				ans.append(safe[closest_1].num)
			else:
				ans.append(safe[closest_2].num)
		elif 0 <= closest_1 < len(safe_pos):
			ans.append(safe[closest_1].num)
		else:
			ans.append(safe[closest_2].num)
	print(" ".join(map(str, ans)))

if __name__ == "__main__":
	main()
