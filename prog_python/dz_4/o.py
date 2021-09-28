
def gcd(a, b):
	if b > a:
		a, b = b, a
	if a % b == 0:
		return b
	return gcd(b, a % b)

def main():
	a = int(input())
	b = int(input())
	print(f"{gcd(a, b)}")

if __name__ == "__main__":
	main()

