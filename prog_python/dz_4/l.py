
def power(a, n):
	result = 1
	if a == 0:
		return(0)
	while n != 0:
		if n > 0:
			result *= a
			n -= 1
		else:
			result /= a
			n += 1
	return(result)

def main():
	a = float(input())
	n = int(input())
	
	print(f"{power(a, n):g}")

if __name__ == "__main__":
	main()

