def sort_2(x, y):
	if x >= y:
		return y, x
	else:
		return x, y

def sort_3(x, y, z):
	if x <= y and x <= z:
		y, z = sort_2(y, z)
		return x, y, z
	elif y <= x and y <= z:
		x, z = sort_2(x, z)
		return y, x, z
	elif z <= y and z <= x:
		x, y = sort_2(x, y)
		return z, x, y


def main():
	x1 = int(input())
	y1 = int(input())
	z1 = int(input())
	x2 = int(input())
	y2 = int(input())
	z2 = int(input())

	x1, y1, z1 = sort_3(x1, y1, z1)
	x2, y2, z2 = sort_3(x2, y2, z2)
	if x1 == x2 and y1 == y2 and z1 == z2:
		print("Boxes are equal")
	elif x1 <= x2 and y1 <= y2 and z1 <= z2:
		print("The first box is larger than the second one")
	elif x1 >= x2 and y1 >= y2 and z1 >= z2:
		print("first box is smaller than the second one")
	else:
		print("Boxes are incomparable")


if __name__ == "__main__":
	main()

