
def gcd(a, b):
	if b > a:
		a, b = b, a
	if a % b == 0:
		return b
	return gcd(b, a % b)

def ReduceFraction(n, m):
	nod = gcd(n, m)
	return int(n / nod), int(m / nod)

def main():
	a = int(input())
	b = int(input())
	
	print(*ReduceFraction(a, b))

if __name__ == "__main__":
	main()

