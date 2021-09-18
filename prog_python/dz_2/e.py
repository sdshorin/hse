def main():
	a = int(input())
	b = int(input())
	c = int(input())
	d = int(input())

	if a == 0:
		if b != 0:
			print("NO")
		else:
			print("INF")
	else:
		res = int(-b / a)
		if -res * a != b:
			print("NO")
		elif res * c + d == 0:
			print("NO")
		else:
			print(res)

		



if __name__ == '__main__':
	main()
