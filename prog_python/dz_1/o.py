MKAD_SIZE_KM = 109

def main():
	speed = int(input())
	time = int(input())
	print((speed * time) % MKAD_SIZE_KM)

if __name__ == "__main__":
	main()
