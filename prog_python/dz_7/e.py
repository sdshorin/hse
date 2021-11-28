
def main():
    anna_q, boris_q = map(int, input().split())
    anna_set = set()
    boris_set = set()
    for i in range(anna_q):
        anna_set.add(int(input()))
    for i in range(boris_q):
        boris_set.add(int(input()))

    crossing = anna_set & boris_set
    ann_unique = anna_set - boris_set
    boris_unique = boris_set - anna_set
    for current_set in [crossing, ann_unique, boris_unique]:
        print(len(current_set))
        print(*sorted(list(current_set)))


if __name__ == "__main__":
    main()
