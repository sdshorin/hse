


def distance(x_1, y_1, x_2, y_2):
	return ((x_2 - x_1)** 2 + (y_2 - y_1)** 2) ** 0.5

def IsPointInCircle(x, y, x_c, y_c, r):
	return distance(x, y, x_c, y_c) <= r

def line_1_is_right(x, y):
	return y <= x

def line_2_is_right(x, y):
	return  -y -2 <= 2 * x

def IsPointInArea(x, y):
	return (y > 0 and (((x + 1)** 2 + (y - 1)** 2) ** 0.5) <=5 and\
		y <= x and not -y -2 < 2 * x) \
			or\
		(y <= 0 and (((x + 1)** 2 + (y - 1)** 2) ** 0.5) >=5 and\
		y > x and not -y -2 < 2 * x)


def main():

	for i in range(-5, 6):
		for j in range(-5, 6):
			print(int(line_1_is_right(j, i)), end=" ")
		print()
	return

	x = float(input())
	y = float(input())
	
	if IsPointInCircle(x, y, -1, 1, 2.0):
		print("YES")
	else:
		print("NO")

if __name__ == "__main__":
	main()
