def main():
	print(*sorted(list(set(map(int, input().split())) & set(map(int, input().split())))))

	

if __name__ == "__main__":
	main()

