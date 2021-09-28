from collections import namedtuple
import os
def main():
	is_num_printed = False
	with open("input.txt") as input:
		with open("output.txt", "w") as output:
			arr_1 = [int(x) for x in input.readline().split()]
			arr_2 = [int(x) for x in input.readline().split()]
			arr_1.sort()
			arr_2.sort()
			arr_1_current = 0
			arr_2_current = 0
			while len(arr_1) > arr_1_current and len(arr_2) > arr_2_current:
				if arr_1[arr_1_current] > arr_2[arr_2_current]:
					arr_2_current += 1
				elif arr_2[arr_2_current] > arr_1[arr_1_current]:
					arr_1_current += 1
				else:
					if is_num_printed:
						output.write(" ")
					is_num_printed = True
					output.write(str(arr_2[arr_2_current]))
					arr_1_current += 1
					arr_2_current += 1
					

if __name__ == "__main__":
	main()
