from collections import defaultdict

def main():
	frequency = defaultdict(int)
	with open("input.txt") as f:
		while True:
			line = f.readline()
			if not line:
				break
			for word in line.split():
				frequency[word] -= 1
	frequency_arr = frequency.items()
	frequency_arr = list(map(lambda arr: (arr[1], arr[0]), frequency_arr))
	frequency_arr.sort()
	for f_num, word in frequency_arr:
		print(word)

if __name__ == "__main__":
	main()
