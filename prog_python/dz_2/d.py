def main():
	n = int(input())
	if 2 <= n % 10 <= 4 and n // 10 != 1:
		print(n, "korovy")
	elif n % 10 == 1 and n // 10 != 1:
		print(n, "korova")
	else:
		print(n, "korov")

if __name__ == "__main__":
	main()
