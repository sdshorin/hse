from collections import defaultdict

def main():
	users = defaultdict(int)
	with open("input.txt") as f:
		while True:
			line = f.readline()
			if not line:
				break
			operation, *data = line.strip().split()
			if operation == "DEPOSIT":
				users[data[0]] += int(data[1])
			elif operation == "WITHDRAW":
				users[data[0]] -= int(data[1])
			elif operation == "BALANCE":
				if data[0] in users:
					print(users[data[0]])
				else:
					print("ERROR")
			elif operation == "TRANSFER":
				users[data[0]] -= int(data[2])
				users[data[1]] += int(data[2])
			elif operation == "INCOME":
				p = 1.0 + int(data[0]) / 100.0
				for name in users:
					if users[name] > 0:
						users[name] = int(users[name] * p)

if __name__ == "__main__":
	main()
