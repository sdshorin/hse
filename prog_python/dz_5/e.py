
def main():
	arr = [int(x) for x in input().split()]
	if not len(arr):
		return
	last = arr[-1]
	for i in range(len(arr) - 1, 0, -1):
		arr[i] = arr[i - 1]
	arr[0] = last
	print(" ".join([str(i) for i in arr]))

	

if __name__ == "__main__":
	main()
