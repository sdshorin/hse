
def main():
	arr = [int(x) for x in input().split()]
	for i in range(len(arr) - 1):
		if arr[i] * arr[i + 1] > 0 or \
			(arr[i] * arr[i + 1] ==  0 and arr[i] + arr[i + 1] >=0):
			print(arr[i], arr[i +1])
			return

	

if __name__ == "__main__":
	main()
