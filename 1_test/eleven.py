

def is_div_by_11(num_str: str):
	numeric_sum = 0
	current_sign = 1
	for char_num in num_str:
		numeric_sum += int(char_num) * current_sign
		current_sign = -1 * current_sign
	return not numeric_sum % 11



def main():
	n_len = int(input())
	n = input()
	if is_div_by_11(n):
		print("YES")
	else:
		print("NO")
	
if __name__ == "__main__":
	main()

