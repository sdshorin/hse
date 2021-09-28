
def main():
	arr = [int(x) for x in input().split()]
	n = int(input())
	
	for i in range(len(arr)):
		if arr[i] < n:
			print(i + 1)
			return
	print(len(arr) + 1)

if __name__ == "__main__":
	main()
