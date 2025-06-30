class stack_interface:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            return None
        self.stack.pop()
    
    def max(self):
        if not self.stack:
            return None
        return max(self.stack)
    

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