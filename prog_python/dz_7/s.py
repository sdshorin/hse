from collections import defaultdict

def main():
	votes = defaultdict(int)
	with open("input.txt") as f:
		while True:
			name = f.readline().strip()
			if not name:
				break
			votes[name] += 1
	total_votes = 0
	for v in votes.values():
		total_votes += v
	votes = list(votes.items())
	votes.sort(key=lambda arr: arr[1], reverse=True)
	if votes[0][1] > total_votes / 2:
		print(votes[0][0])
	else:
		print(votes[0][0])
		print(votes[1][0])

if __name__ == "__main__":
	main()
