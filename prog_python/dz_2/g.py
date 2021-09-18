

def main():
	n = int(input())
	current_pow = 1
	while current_pow <= n:
		print(current_pow, end=" ")
		current_pow *= 2 
	print()

if __name__ == "__main__":
	main()

