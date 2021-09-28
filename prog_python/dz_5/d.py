
def main():
	arr = [int(x) for x in input().split()]
	quantity = 0
	if len(arr):
		quantity = 1
	for i in range(len(arr) - 1):
		if arr[i] != arr[i + 1]:
			quantity += 1
	print(quantity)

	

if __name__ == "__main__":
	main()
