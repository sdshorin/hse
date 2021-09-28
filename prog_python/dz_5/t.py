from collections import namedtuple

def main():
	abiturients = []
	with open("input.txt") as f:
		plases = int(f.readline())
		while True:
			line = f.readline()
			if not line:
				break
			*name, p_1, p_2, p_3 = line.split()
			if int(p_1) < 40 or int(p_2) < 40 or int(p_3) < 40:
				continue
			abiturients.append(int(p_3) + int(p_2) + int(p_1))
	abiturients.sort(reverse=True)
	if len(abiturients) <= plases:
		print(0)
	elif abiturients[plases - 1] == abiturients[plases] == abiturients[0]:
		print(1)
	else:
		last_score = abiturients[plases - 1]
		if abiturients[plases] == last_score:
			while abiturients[plases - 1] == last_score:
				plases -= 1
		print(abiturients[plases - 1])

if __name__ == "__main__":
	main()
