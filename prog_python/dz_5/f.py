
def main():
	arr = [int(x) for x in input().split()]
	uniqum_elements = []
	for x in arr:
		if arr.count(x) == 1:
			uniqum_elements.append(x)
	print(" ".join([str(i) for i in uniqum_elements]))

if __name__ == "__main__":
	main()
