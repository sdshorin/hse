

def main():
	last_num = int(input())
	last_local_max_index = -1
	current_index = 1
	min_distance = 0
	direction = 0
	while last_num != 0:
		current_num = int(input())
		if not current_num:
			break
		current_index += 1
		if direction == 0:
			if current_num > last_num:
				direction = 1
			elif current_num < last_num:
				direction = -1
		else:
			if (direction > 0 and current_num > last_num) or (direction < 0 and current_num < last_num):
				pass
			elif current_num < last_num and direction > 0:
				if last_local_max_index > 0:
					distance = current_index - last_local_max_index
					if distance < min_distance or min_distance == 0:
						min_distance = distance
				last_local_max_index= current_index
				direction = -1
			elif current_num > last_num and direction < 0:
				direction = 1
			else:
				direction = 0
		last_num = current_num
	print(min_distance)

if __name__ == "__main__":
	main()

