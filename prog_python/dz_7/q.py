from collections import defaultdict

def main():
	frequency = defaultdict(int)
	with open("input.txt") as f:
		while True:
			line = f.readline()
			if not line:
				break
			for word in line.split():
				frequency[word] += 1
	frequency = list(frequency.items())
	frequency.sort()
	frequency.sort(reverse=True, key=lambda x: x[1])
	print(frequency[0][0])


if __name__ == "__main__":
	main()
