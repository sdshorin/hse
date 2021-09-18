
def main():
	n = int(input())
	card_num = n
	for i in range(1, n):
		card_num += i - int(input())
	print(card_num)

if __name__ == "__main__":
	main()
