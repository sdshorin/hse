

def main():
	n = int(input())
	k = 0
	current_pow = 1
	while current_pow < n:
		k += 1
		current_pow *= 2 
	print(k)

if __name__ == "__main__":
	main()

