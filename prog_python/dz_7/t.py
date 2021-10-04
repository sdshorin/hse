from collections import defaultdict

def main():
	users = defaultdict(lambda: defaultdict(int))
	with open("input.txt") as f:
		while True:
			line = f.readline().strip()
			if not line:
				break
			name, product, quantity = line.split()
			quantity = int(quantity)
			users[name][product] += quantity
	names = list(users.keys())
	names.sort()
	for name in names:
		print(name + ":")
		products = list(users[name].keys())
		products.sort()
		for product in products:
			print(product, users[name][product])

if __name__ == "__main__":
	main()
