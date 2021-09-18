

def get_divisible_nums(nums: [int], div:int):
	ans_arr = []
	if not div:
		return ans_arr
	for element in nums:
		if element % div == 0:
			ans_arr.append(element)
	return ans_arr

def main():
	num_len = int(input())
	nums = input().split()
	for i in range(len(nums)):
		nums[i] = int(nums[i])
	task_quantity = int(input())
	for i in range(task_quantity):
		div = int(input())
		ans_var = get_divisible_nums(nums, div)
		print(len(ans_var))
		print(" ".join(str(num) for num in ans_var))


if __name__ == "__main__":
	main()

