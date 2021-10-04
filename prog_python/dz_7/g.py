
def main():
	task = set(range(1, int(input()) + 1))
	line = input()
	while line != "HELP":
		nums = set(map( int,  line.split()))
		if input() == "YES":
			task &= nums
		else:
			task -= nums
		line = input()
	print(*sorted(task))


if __name__ == "__main__":
	main()
