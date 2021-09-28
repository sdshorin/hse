
def main():
	arr_len = int(input())
	arr = [int(x) for x in input().split()]
	target = int(input())
	nearest_num = 0
	nearest_diff = -1
	for x in arr:
		if abs(x - target) < nearest_diff or nearest_diff < 0:
			nearest_diff = abs(x - target)
			nearest_num = x
	print(nearest_num)

if __name__ == "__main__":
	main()
