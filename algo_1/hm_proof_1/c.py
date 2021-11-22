
from collections import deque


class Sequence:
    def __init__(self, pow) -> None:
        self.num = 1
        self.pow = pow

    def get_num(self):
        return self.num ** self.pow

    def step(self):
        self.num += 1


def main():
    s_a = Sequence(2)
    s_b = Sequence(3)
    curr_num = 1
    for i in range(int(input())):
        a_elem = s_a.get_num()
        b_elem = s_b.get_num()
        if a_elem < b_elem:
            curr_num = a_elem
            s_a.step()
        elif a_elem > b_elem:
            curr_num = b_elem
            s_b.step()
        else:
            curr_num = b_elem
            s_b.step()
            s_a.step()
    print(curr_num)


if __name__ == "__main__":
    main()
