from collections import namedtuple


def main():
    parties_names = []
    votes = []
    votes_sum = 0
    is_votes_mode = False
    with open("input.txt") as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            if line == "VOTES:":
                is_votes_mode = True
            elif line == "PARTIES:":
                is_votes_mode = False
            elif not is_votes_mode:
                parties_names.append(line)
                votes.append(0)
            elif is_votes_mode:
                assert(line in parties_names)
                votes[parties_names.index(line)] += 1
                votes_sum += 1
    results = []
    Party = namedtuple("Party", ["votes", "name"])
    for i in range(len(votes)):
        results.append(Party(votes[i], parties_names[i]))
    results.sort(key=lambda party: party.name)
    results.sort(reverse=True, key=lambda party: party.votes)

    print("\n".join([results[i].name for i in range(len(results))]))


if __name__ == "__main__":
    main()
