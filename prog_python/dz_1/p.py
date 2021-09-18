def main():
	time = int(input()) % (24 * 60 * 60)
	print(time // 60, time % 60)

if __name__ == "__main__":
	main()
