import math

def find_squares(n, deep, start_index):
	if deep <= 0:
		return False
	if deep == 1:
		if int(n ** 0.5) ** 2 == n:
			return [int(n ** 0.5)]
	for i in range(start_index, int(n ** 0.5) + 1):
		if n == i ** 2:
			return [i]
		if n > i ** 2:
			squares_arr = find_squares(n - i ** 2, deep - 1, i)
			if squares_arr:
				return [i] + squares_arr
		else:
			break
	return False

def main():
	n = int(input())
	squares = find_squares(n, 4, 1)
	if squares:
		print(" ".join(str(i) for i in squares))
	else:
		print(0)

if __name__ == "__main__":
	main()
	