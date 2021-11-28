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
    for i in range(len(votes)):
        votes[i] = votes[i] / votes_sum
    print("\n".join([parties_names[i]
                     for i in range(len(votes)) if votes[i] >= 0.07]))


if __name__ == "__main__":
    main()
