
def main():
    n = int(input())
    results = list(map(int, input().split()))
    best_pos = results.index(max(results))
    vasya_max_distance = 0
    part_results = results[best_pos + 1:]
    for i in range(len(part_results) - 1):
        if part_results[i] % 10 == 5 and part_results[i] > part_results[i + 1]:
            if vasya_max_distance < part_results[i]:
                vasya_max_distance = part_results[i]
    if vasya_max_distance == 0:
        print(0)
        return
    vasya_score = 1
    for i in range(len(results)):
        if results[i] > vasya_max_distance:
            vasya_score += 1
    print(vasya_score)


if __name__ == "__main__":
    main()
