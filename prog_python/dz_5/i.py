
def main():
	arr = [int(x) for x in input().split()]
	dst = -1
	for i in range(len(arr)):
		if arr[i] == 0 and dst == -1:
			dst = i
		elif arr[i] != 0 and dst != -1:
			arr[dst] = arr[i]
			dst += 1
	for i in range(dst, len(arr)):
		arr[i] = 0
	print(" ".join([str(i) for i in arr]))

if __name__ == "__main__":
	main()
