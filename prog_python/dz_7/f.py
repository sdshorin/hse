
def main():
	words = set()
	with open("input.txt") as f:
		while True:
			line = f.readline()
			if not line:
				break
			words |= set(line.split())
	print(len(words))


if __name__ == "__main__":
	main()
