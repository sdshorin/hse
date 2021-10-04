from collections import defaultdict

PLACES = 450

def main():
	parties = defaultdict(int)
	total_voices = 0
	free_places = PLACES
	order = []
	with open("input.txt") as f:
		while True:
			line = f.readline()
			if not line:
				break
			line = line.strip()
			last_space = line.rfind(" ")
			party, votes = line[:last_space], int(line[last_space:])
			parties[party] = votes
			total_voices += votes
			order.append(party)
	first_selective_part = total_voices / PLACES

	result = {}
	ost = []
	for party in parties:
		result[party] = int(parties[party] / first_selective_part)
		ost.append((parties[party] / first_selective_part - int(parties[party] / first_selective_part), parties[party], party))
		free_places -= result[party]
	if free_places > 0:
		ost.sort(reverse=True)
		for party_info in ost:
			result[party_info[2]] += 1
			free_places -= 1
			if free_places == 0:
				break
	for party in order:
		print(party, result[party])



if __name__ == "__main__":
	main()
