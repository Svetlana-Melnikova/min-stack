class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        if len(self.stack) == 3:
            self.stack.pop(0)
            self.min_stack = []

            for num in self.stack:
                if not self.min_stack or num <= self.min_stack[-1]:
                    self.min_stack.append(num)

        self.stack.append(value)

        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            raise IndexError("Stack is empty")

        value = self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()

        return value

    def top(self):
        if not self.stack:
            raise IndexError("Stack is empty")

        return self.stack[-1]

    def get_min(self):
        if not self.min_stack:
            raise IndexError("Stack is empty")

        return self.min_stack[-1]

stack = MinStack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.get_min())
stack.pop()
print(stack.top())
print(stack.get_min())