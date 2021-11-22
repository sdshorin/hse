
from collections import deque

USED = 26

def main():
    q, s_q = map(int, input().split())
    s = input()
    finded = [0] * 26
    seq = []
    for i in range(26):
        seq.append([])
        for j in range(26):
            seq[i].append(0)
        seq[i].append(False)
    data = [0] * 26
    ans = 0
    for i in range(s_q):
        inp = input()
        # inp = debug_s[i]
        seq[ord(inp[0]) - ord("a")][ord(inp[1]) - ord("a")] = 1
        seq[ord(inp[0]) - ord("a")][USED] = True
    for i in range(len(s) - 1, -1, -1):
        elem = s[i]
        if seq[ord(elem) - ord("a")][USED]:
            first_elem = ord(elem) - ord("a")
            for i in range(26):
                if seq[first_elem][i]:
                    ans += data[i]
        data[ord(elem) - ord("a")] += 1
    print(ans)



if __name__ == "__main__":
    main()
