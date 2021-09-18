


def xor(a, b):
	return int((a and not b) or (not a and b))

def main():
	a = int(input())
	b = int(input())
	
	print(f"{xor(a, b)}")

if __name__ == "__main__":
	main()
