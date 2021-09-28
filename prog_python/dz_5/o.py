
def main():
	class_tops = [0 ,0, 0]
	try:
		while True:
			line = input()
			class_num, result = [int(x) for x in line.split()[2:]]
			if class_tops[class_num - 9] < result:
				class_tops[class_num - 9] = result
	except EOFError as e:
		pass
	print(" ".join([str(i) for i in class_tops]))


if __name__ == "__main__":
	main()
