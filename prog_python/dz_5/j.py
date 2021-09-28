
def main():
	arr = [int(x) for x in input().split()]
	frequent_num = 0
	frequent_quan = -1
	for x in arr:
		if arr.count(x) > frequent_quan:
			frequent_quan = arr.count(x)
			frequent_num = x
	print(frequent_num)

if __name__ == "__main__":
	main()
