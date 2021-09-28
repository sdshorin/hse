
def print_num_deffer():
	n = int(input())
	if n != 0:
		print_num_deffer()
	print(n)

def main():
	print_num_deffer()

if __name__ == "__main__":
	main()
	
