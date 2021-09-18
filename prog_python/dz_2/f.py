


def is_cross(l1, r1, l2, r2):
	return l1 <= l2 <= r1 or l1 <= r2 <= r1 or l2 <= l1 <= r2 or l2 <= r1 <= r2

def get_distance(l1, r1, l2, r2):
	if is_cross(l1, r1, l2, r2):
		return 0
	if r1 < l2:
		return l2 - r1
	if r2 < l1:
		return l1 - r2
	assert(false)

def main():
	l1 = int(input())
	r1 = int(input())
	l2 = int(input())
	r2 = int(input())
	l3 = int(input())
	r3 = int(input())

	if int(is_cross(l1, r1, l2, r2)) + \
		int(is_cross(l3, r3, l2, r2)) + \
		int(is_cross(l3, r3, l1, r1)) >= 2:
		print(0)
		return
	if get_distance(l2, r2, l3, r3) <= r1 - l1:
		print(1)
		return
	if get_distance(l1, r1, l3, r3) <= r2 - l2:
		print(2)
		return
	if get_distance(l1, r1, l2, r2) <= r3 - l3:
		print(3)
		return
	print(-1)

if __name__ == "__main__":
	main()

