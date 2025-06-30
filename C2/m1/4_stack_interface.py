class stack_interface:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, data):
        self.stack.append(data)
        if not self.max_stack or data >= self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        if not self.stack:
            return None
        self.stack.pop()
        self.max_stack.pop()

    def max(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]


if __name__ == "__main__":
    n = int(input())
    stack = stack_interface()
    result = []
    for _ in range(n):
        command = input().strip()
        if command.startswith("push"):
            _, value = command.split()
            stack.push(int(value))
        elif command == "pop":
            stack.pop()
        elif command == "max":
            result.append(stack.max())
        else:
            print("Invalid command")

    for res in result:
        print(res)
