
def main():
	days, parties_q = map(int, input().split())
	weekends = {i for i in range(6, days + 1, 7)} | {i for i in range(7, days + 1, 7)}
	drop_days = set()
	for _ in range(parties_q):
		a, b = map(int, input().split())
		drop_days |={ i for i in range(a, days + 1, b)}
	drop_days -= weekends
	print(len(drop_days))

if __name__ == "__main__":
	main()
