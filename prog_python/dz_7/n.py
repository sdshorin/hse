from collections import defaultdict


def main():
    frequency = defaultdict(int)
    with open("input.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            for word in line.split():
                print(frequency[word], end=" ")
                frequency[word] += 1


if __name__ == "__main__":
    main()
