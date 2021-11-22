
from collections import deque


class Stack:
    def __init__(self) -> None:
        self.arr = []
        self.is_valid = True

    def push(self, num):
        self.arr.append(num)

    def pop(self, num):
        if self.is_valid:
            self.is_valid = self.arr.pop() == num


class Queue:

    def __init__(self) -> None:
        self.queue = deque()
        self.is_valid = True

    def push(self, num):
        self.queue.append(num)

    def pop(self, num):
        if self.is_valid:
            self.is_valid = self.queue.popleft() == num


def main():
    stack = Stack()
    queue = Queue()
    for i in range(int(input())):
        command = input()
        num = int(command.split()[1])
        if command.startswith("push"):
            queue.push(num)
            stack.push(num)
        elif command.startswith("pop"):
            queue.pop(num)
            stack.pop(num)
    if stack.is_valid and queue.is_valid:
        print("both")
    elif queue.is_valid:
        print("queue")
    elif stack.is_valid:
        print("stack")
    else:
        print("none")


if __name__ == "__main__":
    main()
