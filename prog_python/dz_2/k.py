

def main():
	last_num = int(input())
	accum = 1
	max_len = 1
	direction = 0
	while last_num != 0:
		current_num = int(input())
		if not current_num:
			break
		if direction == 0:
			if current_num > last_num:
				direction = 1
				accum = 2
			elif current_num < last_num:
				direction = -1
				accum = 2
		else:
			if (direction > 0 and current_num > last_num) or (direction < 0 and current_num < last_num):
				accum += 1
			elif current_num < last_num and direction > 0:
				direction = -1
				accum = 2
			elif current_num > last_num and direction < 0:
				direction = 1
				accum = 2
			else:
				direction = 0
				accum = 1
		if accum > max_len:
			max_len = accum
		last_num = current_num
	print(max_len)

if __name__ == "__main__":
	main()

