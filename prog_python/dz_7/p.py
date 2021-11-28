from collections import defaultdict


def main():
    votes = defaultdict(int)
    with open("input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            party, vote = line.strip().split()
            votes[party] += int(vote)
    all_candidates = sorted(votes.keys())
    for candidat in all_candidates:
        print(candidat, votes[candidat])


if __name__ == "__main__":
    main()
