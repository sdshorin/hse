def main():
	schoolboy_q = int(input())
	all_known = None
	one_known = None
	
	for i in range(schoolboy_q):
		lang_q = int(input())
		schoolboy_known = set()
		for _ in range(lang_q):
			schoolboy_known.add(input())
		if one_known == None:
			one_known = schoolboy_known.copy()
			all_known = schoolboy_known.copy()
		else:
			all_known &= schoolboy_known
			one_known |= schoolboy_known
	print(len(all_known))
	print("\n".join(all_known))
	print(len(one_known))
	print("\n".join(one_known))

if __name__ == "__main__":
	main()