
def main():
	arr = [int(x) for x in input().split()]
	if not len(arr):
		return
	_min = 100000
	for i in range(len(arr)):
		if arr[i] < _min and arr[i] > 0:
			_min = arr[i]
	print(_min)	

if __name__ == "__main__":
	main()
