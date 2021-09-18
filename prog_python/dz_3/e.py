
def main():
	s = input()
	first_pos = s.find("h")
	last_pos_pos = s.rfind("h")
	if first_pos == -1:
		return
	elif first_pos == last_pos_pos:
		return 
	else:
		print(s[:first_pos] + s[last_pos_pos + 1:])

if __name__ == "__main__":
	main()
