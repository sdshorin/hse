
from bisect import bisect_left


def main():
	diego_num = int(input())
	diego_stikers_dict = {}
	for i in input().split():
		diego_stikers_dict[int(i)] = 1
	diego_stikers = list(diego_stikers_dict.keys())
	diego_stikers.sort()
	collector_num = int(input())
	collectors_collections = [int(i) for i in input().split()]
	for collection in collectors_collections:
		print(bisect_left(diego_stikers, collection))


	
if __name__ == "__main__":
	main()

