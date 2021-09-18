
def main():
	max_palindrom = int(input())
	current_p_len = 1
	counter = 0
	is_palindrom_finded = True
	while is_palindrom_finded:
		is_palindrom_finded = False
		p_part = 1 #10 ** ((current_p_len - 1) // 2)
		while p_part < 10 ** ((current_p_len - 1) // 2 + 1):
			if p_part % 10 == 0:
				p_part += 1
				continue
			palindrom = 0
			part_str = str(p_part).zfill((current_p_len + 1) // 2)
			if current_p_len % 2 == 0:
				palindrom = int(str(part_str)[::-1] + str(part_str))
			else:
				center = str(part_str)[0]
				palindrom = int(center)
				if current_p_len > 1:
					part = str(part_str)[1:]
					palindrom = int(str(part)[::-1] + center + str(part))
			if palindrom <= max_palindrom:
				counter += 1
				is_palindrom_finded = True
			# print(palindrom)
			p_part += 1
		current_p_len += 1
	print(counter)

if __name__ == "__main__":
	main()

